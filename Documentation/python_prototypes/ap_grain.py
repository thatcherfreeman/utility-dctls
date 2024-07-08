import numpy as np

from PIL import Image

from scipy.signal import convolve2d

from scipy.ndimage import gaussian_filter

from scipy.special import erfinv, erf

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt
import argparse


GAMMA = 2.4


def show_image(array):

    # Re-gamma and convert to 8 bits

    result = Image.fromarray(np.uint8(array**(1. / GAMMA) * 255))

    result.show()

    return result


def open_image(path):

    # Open, un-gamma and convert to monochrome using luminance

    image = Image.open(path)

    im = (np.array(image) / 255.)**GAMMA

    return im[:,:,0], im[:,:,1], im[:,:,2]


def create_crystal(width, n, rotation):

    # w is the width of the kernel, aka "grain". Needs to be odd.

    # n is number of vertices: 3 for triangle, 4 for square, 5 for pentagon, etc.

    # see https://math.stackexchange.com/a/4160104/498090

    # rotation is an angle in radians

    # blur controls how fuzzy the crystal edges are


    # Spatial coordinates rounding error

    eps = 1. / width

    radius = max(int((width - 1) / 2.), 1) # exact if width is odd

    kernel = np.empty((width, width))


    for i in range(width):

        for j in range(width):

            # get normalized kernel coordinates from center in [-1 ; 1]

            x = i / radius - 1.

            y = j / radius - 1.


            # get current radial distance from kernel center

            r = np.hypot(x, y)


            # get the radial distance at current angle of the shape envelope

            M = np.cos(np.pi / n) / np.cos((2. * np.arcsin(np.cos(n * (np.arctan2(y, x) + rotation))) + np.pi) / (2. * n))


            # write 1 if we are inside the envelope of the shape, else 0

            kernel[i, j] = (M >= r - eps)


    return kernel



def pick_crystal(size, std):

    # Pick one crystal size, shape and orientation based on random dice rolls

    rng = np.random.default_rng()


    dice_shape = np.clip(rng.normal(6, 1.5), 3, 10)

    dice_rotation = np.random.rand() * 2. * np.pi


    log_normal_var = np.random.lognormal(mean=np.log(size), sigma=std)

    random_size = int(min(max(log_normal_var, 1), 3 * size))


    # ensure kernel size is odd

    if random_size % 2 == 0.:

        random_size += 1


    return create_crystal(random_size, dice_shape, dice_rotation)


def distribution_to_variable(population, sigma):

    # Find t so the normal centered unit gaussian distribution G(x, mu=0, sigma=1)

    # contains the population ratio below x = t.

    # population is in[0; 1]

    return erfinv(2. * population - 1.) * np.sqrt(2.) * sigma


def variable_to_distribution(x, sigma=1.):

    # Find the ratio of the population of the normal centered unit

    # gaussian distribution G(x, mu=0, sigma=1)

    # contained below x

    return (1. + erf(x / (sigma * np.sqrt(2)))) / 2.


def filling_to_rand_variable(x):

    # Map a filling ratio with a gaussian distribution variable

    # fitting in [0; 1] :

    # return 1.3790633 * x*1.34123704 / np.abs(x - 1)**0.27288849

    # fitting in [0; 0.8] :

    return 1.12139063 * x*1.05577624 / np.abs(x - 1)**0.34443235


def grainify(image, filling=0.9, size=9, n=20, std=1):

    """

    Params:

        - image (array): B&W image or single color channel

        - filling (float): ratio of surface filling with AgX crystals.

        - size (int): average pixel size of the grain (odd values only)

        - n (int): number of layers of silver halide.

        - std (float): the standard deviation of the log-normal distribution of crystal sizes.


    Photo emulsions are 10 to 15 μm thick, [1][2]

        - non-tabular grains have a typical diameter between 0.5 and 0.7 μm (up to 3μm) [1][2]

        - tabular grains have a thickness of 0.12 micrometer but are used for color emulsions (×3) [4]

    That gives us 14 to 40 crystal layers in practice.


    The surface filling ratio was 15% of Ilford emulsions in the 1960's. [1]

    Visual results of the simulation indicate Ilford Delta 100 could be around 25 %.


    References :

         [1] https://cds.cern.ch/record/870005/files/p129.pdf

         [2] https://www.epfl.ch/labs/gdp/wp-content/uploads/2019/09/PC2_Lesson_10.pdf

         [3] https://pubs.acs.org/doi/pdf/10.1021/bk-1982-0200.ch001

         [4] https://www.jstage.jst.go.jp/article/photogrst1964/49/6/49_6_499/_pdf


    """

    result = np.zeros_like(image)

    crystals = np.zeros_like(image)


    final_filling = 0.

    sigma = filling_to_rand_variable(filling)

    layer_density = image / n


    for i in range(n):

        # Init a random crystal shape and size for the current layer

        crystal_area = 0

        while crystal_area == 0.:

            # Some shapes applied on small kernel sizes lead to null kernels.

            # In that case, try again.

            crystal = pick_crystal(size, std)

            crystal_area = crystal.sum()


        # Ensure a constant surface filling over layers, no matter the crystal size

        n_a = filling * image.size / crystal_area

        value = filling if crystal_area == 1 else sigma / crystal_area

        bound = distribution_to_variable(value, np.sqrt(n_a))


        # Lightness value for seeds

        layer = np.clip(layer_density, 0, (image - result))


        # Init random seeds over the surface of the layer

        seeds = np.where(np.random.normal(n_a, np.sqrt(n_a), image.shape) < n_a + bound, layer, 0.)


        # Grow the crystals by convolving seeds with non-normalized crystal kernel.

        grains = convolve2d(seeds, crystal, mode='same', boundary='symm')


        # Crystal kernel is not normalized (to enlarge seeds), meaning when 2 crystals

        # overlap, energy is added as if AgX captured more photons than available.

        # Normalize it now for energy conservation.

        grains = np.where(grains > layer, layer, grains)


        result += grains


    # Adjust global exposure to match the original

    coef = np.mean(image) / np.mean(result)

    print("exposure coef:", coef)

    grainy = np.clip(result * coef, 0., 1.)


    # Printing model of opacity : fully white on paper is fully opaque on negative

    # so grains should not appear there. Use alpha blending to mix grain with the original smooth pic.

    mask = 1. - image # assuming white = 1, otherwise normalize first

    return np.clip(mask * grainy + (1. - mask) * image, 0., 1.), final_filling / n

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Grainify an image.')
    parser.add_argument('input', type=str, help='Input image file path')
    parser.add_argument('output', type=str, help='Output image file path')
    parser.add_argument('--filling', type=float, default=0.25, help='Ratio of surface filling with AgX crystals')
    parser.add_argument('--size', type=int, default=7, help='Average pixel size of the grain (odd values only)')
    parser.add_argument('--n', type=int, default=30, help='Number of layers of silver halide')
    parser.add_argument('--std', type=float, default=0.25, help='Standard deviation of the log-normal distribution of crystal sizes')
    parser.add_argument('--bw', action='store_true', help='Run in black and white mode')
    args = parser.parse_args()

    red, green, blue = open_image(args.input)

    if args.bw:
        neutral = 0.2 * red + 0.7 * green + 0.1 * blue
        grainy_neutral, fill_ratio = grainify(neutral, filling=args.filling, size=args.size, n=args.n, std=args.std)
        grainy = np.stack([grainy_neutral, grainy_neutral, grainy_neutral], axis=-1)
    else:
        grainy_red, fill_ratio = grainify(red, filling=args.filling, size=args.size, n=args.n, std=args.std)
        grainy_green, fill_ratio = grainify(green, filling=args.filling, size=args.size, n=args.n, std=args.std)
        grainy_blue, fill_ratio = grainify(blue, filling=args.filling, size=args.size, n=args.n, std=args.std)
        grainy = np.stack([grainy_red, grainy_green, grainy_blue], axis=-1)

    to_save = show_image(grainy)

    to_save.save(args.output) # optional