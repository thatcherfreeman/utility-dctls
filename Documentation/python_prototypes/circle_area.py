import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    radius = float(input("Enter the radius of the circle: "))
    image_width = int(radius * 2) + 3
    image_height = image_width

    areas = np.zeros((image_height, image_width))
    distances = np.zeros((image_height, image_width))

    circle_center = (image_height // 2, image_width // 2)

    # Identify how much each pixel in the image `areas` overlaps with the circle, using monte carlo approach for each pixel

    num_samples_per_pixel = 2000

    for i in range(image_height):
        for j in range(image_width):
            distances[i, j] = math.sqrt((i - circle_center[0])**2 + (j - circle_center[1])**2)
            for _ in range(num_samples_per_pixel):
                x = i + np.random.uniform(-0.5, 0.5)
                y = j + np.random.uniform(-0.5, 0.5)
                if (x - circle_center[0])**2 + (y - circle_center[1])**2 <= radius**2:
                    areas[i, j] += 1
    areas /= num_samples_per_pixel

    plt.imshow(areas, cmap='hot')
    plt.show()

    # plot areas as a function of distances
    plt.plot(distances.flatten(), areas.flatten(), 'o')
    plt.show()


if __name__ == '__main__':
    main()