# Utility DCTLS
These are DCTLs that I have developed.

Support me at: [https://www.buymeacoffee.com/thatcherfreeman](https://www.buymeacoffee.com/thatcherfreeman)

## Contents
- [Utility DCTLS](#utility-dctls)
    - [Contents](#contents)
- [Installation](#installation)
- [The Fuses](#the-fuses)
    - [Fuses](#fuses)
        - [DCTL Interpreter](#dctl-interpreter)
        - [FrameAvg Fuse](#frameavg-fuse)
        - [HDR Blending Fuse](#hdr-blending-fuse)
        - [Linear Exposure Fuse](#linear-exposure-fuse)
        - [LUT Smoother Fuse](#lut-smoother-fuse)
        - [Merge Adjacent Fuse](#merge-adjacent-fuse)
        - [MTF Curve Fuse](#mtf-curve-fuse)
        - [Periodic Frame Sampler Fuse](#periodic-frame-sampler-fuse)
        - [Pixel Logger Fuse](#pixel-logger-fuse)
        - [Recenter Fuse](#recenter-fuse)
        - [RotateImage Fuse](#rotateimage-fuse)
- [The DCTLs:](#the-dctls)
    - [Effects](#effects)
        - [Bleach Bypass DCTL](#bleach-bypass-dctl)
        - [Field Curvature DCTL](#field-curvature-dctl)
        - [Film Curve DCTL](#film-curve-dctl)
        - [Film Grain DCTL](#film-grain-dctl)
        - [Gain Normalization](#gain-normalization)
        - [Halation DCTL](#halation-dctl)
        - [Hue Curve DCTL](#hue-curve-dctl)
        - [Lens Distortion DCTL](#lens-distortion-dctl)
        - [Linear Contrast DCTL](#linear-contrast-dctl)
        - [Matrix Manipulator](#matrix-manipulator)
        - [MTF Curve DCTL](#mtf-curve-dctl)
        - [Parametric Blur DCTL](#parametric-blur-dctl)
        - [Photon Noise DCTL](#photon-noise-dctl)
        - [Random Channel Mixer](#random-channel-mixer)
        - [Random Contrast Curve](#random-contrast-curve)
        - [Random Linear Contrast](#random-linear-contrast)
        - [RGB Linear Contrast DCTL](#rgb-linear-contrast-dctl)
        - [Subtractive Saturation DCTL](#subtractive-saturation-dctl)
        - [Tone Mapping DCTL](#tone-mapping-dctl)
        - [Vignette DCTL](#vignette-dctl)
    - [Operations](#operations)
        - [Addition Function DCTL](#addition-function-dctl)
        - [Clamp DCTL](#clamp-dctl)
        - [Color Generator DCTL](#color-generator-dctl)
        - [Color Sampler DCTL](#color-sampler-dctl)
        - [Cross Product DCTL](#cross-product-dctl)
        - [Dot Product DCTL](#dot-product-dctl)
        - [Gamma Function DCTL](#gamma-function-dctl)
        - [Invert DCTL](#invert-dctl)
        - [Log Function](#log-function)
        - [Luminance Qualifier](#luminance-qualifier)
        - [Matrix](#matrix)
        - [Modulo Function DCTL](#modulo-function-dctl)
        - [Multiplication Function DCTL](#multiplication-function-dctl)
        - [Polynomial Kernel DCTL](#polynomial-kernel-dctl)
        - [Power Function DCTL](#power-function-dctl)
        - [Projective Transformation Matrix DCTL](#projective-transformation-matrix-dctl)
        - [Root Polynomial Degree 2 DCTL](#root-polynomial-degree-2-dctl)
        - [Scaled Gamut DCTL](#scaled-gamut-dctl)
        - [Sigmoid Function DCTL](#sigmoid-function-dctl)
        - [Sigmoid Kernel DCTL](#sigmoid-kernel-dctl)
        - [Softmax DCTL](#softmax-dctl)
        - [Tanh Function DCTL](#tanh-function-dctl)
        - [Unit Length DCTL](#unit-length-dctl)
        - [Vector Norm DCTL](#vector-norm-dctl)
    - [Utilities](#utilities)
        - [ACES Exposure DCTL](#aces-exposure-dctl)
        - [Bit Depth Estimator DCTL](#bit-depth-estimator-dctl)
        - [Blanking Checker DCTL](#blanking-checker-dctl)
        - [Brand Colors DCTL](#brand-colors-dctl)
        - [Channel Viewer DCTL](#channel-viewer-dctl)
        - [Chroma Subsampling Chart DCTL](#chroma-subsampling-chart-dctl)
        - [Chroma Subsampling DCTL](#chroma-subsampling-dctl)
        - [CIELUV DCTL](#cieluv-dctl)
        - [ColorChecker DCTL](#colorchecker-dctl)
        - [Color Picker DCTL](#color-picker-dctl)
        - [Color Ramp DCTL](#color-ramp-dctl)
        - [Cube Rotate DCTL](#cube-rotate-dctl)
        - [Cylindrical DCTL](#cylindrical-dctl)
        - [DaVinci LGGO DCTL](#davinci-lggo-dctl)
        - [DaVinci Tone Mapping DCTL](#davinci-tone-mapping-dctl)
        - [Exposure Chart DCTL](#exposure-chart-dctl)
        - [False Color Generator DCTL](#false-color-generator-dctl)
        - [Grid Chart DCTL](#grid-chart-dctl)
        - [Frequency Test Chart DCTL](#frequency-test-chart-dctl)
        - [Gamma Curve DCTL](#gamma-curve-dctl)
        - [Gamut Primaries Conversion DCTL](#gamut-primaries-conversion-dctl)
        - [Gradient Smoothness Chart DCTL](#gradient-smoothness-chart-dctl)
        - [Legacy Log Curve DCTL](#legacy-log-curve-dctl)
        - [Levels Converter](#levels-converter)
        - [Log Curve DCTL](#log-curve-dctl)
        - [Luminance](#luminance)
        - [Output Blanking DCTL](#output-blanking-dctl)
        - [Polarity Checker](#polarity-checker)
        - [Printer Lights](#printer-lights)
        - [Pure Log Curve DCTL](#pure-log-curve-dctl)
        - [Quantize](#quantize)
        - [Rebind LGGO DCTL](#rebind-lggo-dctl)
        - [Resize Checker DCTL](#resize-checker-dctl)
        - [RGB Chips DCTL](#rgb-chips-dctl)
        - [Safety Lines DCTL](#safety-lines-dctl)
        - [SNR Checker DCTL](#snr-checker-dctl)
        - [Spherical DCTL](#spherical-dctl)
        - [T-Log Curve](#t-log-curve)
        - [Waveform Guides](#waveform-guides)
        - [White Mask DCTL](#white-mask-dctl)


# Installation
DCTLs should be placed in the following folder:

**MacOS**: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT`

**Windows**: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT`

Fuses should be placed in the following folder to install them into the Fusion page of DaVinci Resolve:

**MacOS**: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Fuses`

**Windows**: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Fuses`

Fuses should also be placed in the following folder to install them for Fusion Studio:

**MacOS**: `/Library/Application Support/Blackmagic Design/Fusion/Fuses`

**Windows**: `C:\ProgramData\Blackmagic Design\Fusion\Fuses`

If a DCTL is not working, you can usually find logs in these directories. If you find that there is a problem, make an Issue on Github with your OS and Resolve version so I can fix it.

**MacOS**: `[Your user directory]/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs/davinci_resolve.log` or `/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs/davinci_resolve.log`

**Windows**: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\logs\davinci_resolve.log` or `[Your user directory]\AppData\Blackmagic Design\DaVinci Resolve\Support\logs\davinci_resolve.log`

# The Fuses

## Fuses


---

### DCTL Interpreter
Adds support for DCTLs within Fusion Studio rather than just Resolve. This is done by reading in a DCTL file and any headers, then rewriting several parts of the source code so it can be run natively within the Fuse DCTL framework (which is somewhat different than the Resolve DCTL framework).

#### Parameters
**DCTL File**: Allows you to specify a .dctl file, anywhere on your system.

**Debug to Console**: Prints out the changes made to the source code and the quantity of captured params.

**Explicitly Typecast Builtin Funcs**: The Fuse DCTL framework has a bug where builtin functions like `_exp2f()`, when provided with an integer argument, will cause the DCTL to fail to build. As a workaround, if you check this box I parse all the code and inject the appropriate type cast to each parameter. This can have some performance impact if your DCTL is large enough as it's a lot of string manipulations that would take place every frame.

**Don't run the DCTL Code**: Self explanatory, If your DCTL is causing Fusion to crash, checking this box might help you help me debug it. Doesn't always stop Fusion from crashing though.


---

### FrameAvg Fuse
Blends together several frames, can be used to retime projects shot at high frame rates. Should certainly be used with a float input, and likely be used with a Linear input.

#### Parameters
**Number of Frames**: quantity of frames to look ahead, including this frame.

**Frame Hold**: How long to hold the current frame (units are quantity of frames), allowing you to control it so that your resulting frames average nonoverlapping input frames.

#### Examples:
Suppose you shot a video at 240fps, 360degree shutter. To simulate 24fps 360degree shutter, you would set Number of Frames to 10, Frame Hold to 10. To simulate 30fps 180degree shutter, you would set Number of Frames to 4, Frame Hold to 8.


---

### HDR Blending Fuse
For the purpose of stitching HDR (multiple exposure composites) images.

#### How to use
1. Take two images of the same scene at different exposures.
2. Load the images into post and correct the exposures to match.
3. Take the image with the lower clipping point and connect it to the background of this Fuse. Connect the other image with the highlight detail to the foreground of the fuse
4. Set the threshold in the Fuse to just below the clipping point in the background image, set the feathering to be around 10% lower than that. Consider bumping the Blur to 1.0 to account for slight misalignment between the images.

#### Parameters
**Foreground Threshold**: Threshold above which the foreground image is copied in.

**Feather Threshold**: For background code values between Feather Threshold and Foreground Threshold, the two layers are blended together.

**Blur Amount**: Indicates how much to blur the mask resulting from the above two thresholds.

**Show Mask**: Shows the mask used. Each of the three channels is masked individually.

**Channel Blend Criteria**: If you choose "Individual Channels", then this checks each background channel independently. If a channel exceeds the Threshold, then it is replaced with the foreground. If you choose "Largest Channel", then if *any* of the channels exceed the threshold, the foreground will be used.

---

### Linear Exposure Fuse
Simply multiplies the input values by `2^x`, where `x` is the specified Exposure (Stops) value. Expects a Linear input.

#### Parameters
**Exposure (Stops)**: Exposure compensation to make in stops.

---
### LUT Smoother Fuse
Applies a 3D gaussian blur convolution on a LUT. Generate a **Horizontal** HALD image in Fusion via the LUTCubeCreator node. Send it through whatever operations you want and then put it into the LUT Smoother Fuse, which will then crunch numbers and spit out the smoothed LUT.

#### Parameters
**Saturated Blur Strength**: Controls the strength of the blur in more saturated areas. Tune by eye, the fuse is slower the larger this value is set to.

**Achromatic Blur Strength**: Controls the strength of the blur in the less saturated areas.

**Saturation Threshold**: Saturation threshold at which we will start using the Saturated Blur Strength. When set to 0.0, the cube is blurred using only the saturated blur strength, otherwise it fades from the Achromatic Blur Strength at sat = 0.0 to the Saturated Blur Strength at Sat = Threshold.



---

### Merge Adjacent Fuse
Simply sticks the foreground image to be adjacent to the background image, really quickly so that it doesn't require any work or the necessary three or four nodes. You can choose what direction the two images are concatenated.



---

### MTF Curve Fuse
This is a higher quality version of the MTF Curve DCTL. Here, we provide 5 frequency bands in which the lower end number of line-pairs per mm can be specified, and the computation of the frequency bands is done in a higher quality way. Importantly, this Fuse requires that your input image is a Float16 or Float32 type image, and it works best on a Log state image. I do not recommend using it with a Linear state image, and I would also recommend clamping the input to be non-negative. This Fuse works using several different discrete frequency bands rather than via a fourier transform, but it largely gives good looking results regardless.

#### Parameters
**Gate Width**: The mm width of your frame.

**Band 1-5 LP/mm**: This indicates where the frequency band should start for bands 1-5. Technically the resizing operation is imperfect, so if you're trying to match a chart, lower each value slightly. IE if you have a chart with 20 LP/mm on it, set the band to start early at about 5 LP/mm below the value you're trying to target.

**Band 1-5 Contrast**: This allows you to control the contrast level of each band on a scale from 0 to 2. 1.0 is neutral, and higher is more contrast.

**Debug Mode**: This pull-down allows you to figure out what each band targets. You can choose from None (runs the plugin normally), Low Pass Mode (shows you the information that's too low frequency to be captured in this band), High Pass Mode (shows the information that's in this band), and High Pass Gray Mode (Same as High Pass mode, but normalized to 0.5 so that the frequency data in this band is more visible).

**Debug Band**: Allows you to choose which band will be shown in the Debug mode.

**Performance Mode**: Quality does the right thing, but if you find that it's too slow, you can change this to Performance. Performance uses a lower quality computation for the low frequency information, and importantly it disables all bands except for the last two.

**Method**: Choose between Quotient and Difference. In most real-world scenarios, the Quotient method provides better looking results, but the Difference method performs more accurately on zebra striped test charts. Here's the math:
```
quotient_out := (input_value / low_pass5)^band5_contrast * (low_pass5 / low_pass4)^band4_contrast * ... * low_pass1
difference_out := (input_value - low_pass5)*band5_contrast + (low_pass5 - low_pass4)*band4_contrast + ... + low_pass1
```


---

### Periodic Frame Sampler Fuse
Samples the input image at the specified frame interval. Suppose the current frame time is `Destination Time Start`, and you want to be looking at the input image at frame `Source Time Start`, and you want the next frame outputted from this Fuse to be at `Source Time Start + Period * 1` and so on, then this is the Fuse for you.

Essentially, we will compute:

`(current_time - destination_time_start) * period + source_time_start` and return the frame at this time.

#### Parameters
**Source Time Start**: Frame number we should consider to be the "First Frame" of the input image.

**Destination Time Start**: Frame number at which we should output the `Source Time Start` frame.

**Period**: As time progresses one frame, this indicates how many frames later we should sample from the source image.




---

### Pixel Logger Fuse
Samples the specified pixel in the image, then prints out the frame number and rgb values to console.

#### Instructions
1. Place it somewhere in the render path of your pipeline (it could simply be "rendered" by being sent to the viewer)
2. Go to the start of the video file
3. Clear the console logs with the CLS button
4. Hit the Reload button at the top of the Fuse
5. Hit play or scrub through frames, whenever the frame number changes, the Fuse will print to the log.
6. Copy and paste the contents of the log to a CSV file or spreadsheet or something, maybe filter by tags later.

**Note**: In order to make this thing print out on every frame change, I needed the Process function to be called on every frame change and had to use a hack to disable caching. This means that this Fuse and everything downstream of it should be uncachable and this will negatively impact playback and render performance. You probably want to put this at the end of the pipeline.

#### Parameters
**Pixel Location X/Y**: The x/y coordinates of the pixel you want to sample from.

**Tags**: Any tags you want to add to the end of the line. I figure if you have multiple of these nodes in your pipeline, then you'll probably want to be able to distinguish between them by setting different tags.

**Log Header**: If you're on Frame 0 and you hit Reload when this is checked, it'll print out a`frame,red,green,blue[,tags]`, which would make it useful when copying and pasting your console into spreadsheet software via csv. Uncheck this if you don't want that bit to be printed out.


---
### Recenter Fuse
Allows you to specify a source point that you want to move to a destination coordinate. Useful if you need to align a variety of images that only differ in terms of translation.

#### Parameters
**Mode**: Indicate whether to look at the source image (pre-translation) or destination image (after translation)

**Copy Src to Dest/Dest to Src**: Allows you to copy the original pixel location to the new pixel location or vice versa, respectively.

**Original Pixel Location**: X,Y coordinates of some pixel in the source image

**New Pixel Location**: X,Y coordinates that indicate the desired destination location of the Original Pixel Location.


---
### RotateImage Fuse
Rotate the input image in increments of 90 degrees, resizing the canvas as necessary.

#### Parameters
**Rotation**: Indicate the number of degrees to rotate the image, counterclockwise.

---

# The DCTLs:

## Effects


---

### Bleach Bypass DCTL
Applies a beach bypass look to the image. Expects a Linear image. Uses a custom Overlay implementation designed for Linear images.

The underlying implementation was completely replaced on May 11, 2024 for improved continuity. You can download the previous version [here](https://github.com/thatcherfreeman/utility-dctls/blob/5e8f7adeba60c4697f35508079012f3f7becb285/Effects/Bleach%20Bypass.dctl).

#### DCTL Parameters
**Saturation**: Indicates how saturated or desaturated the result should be.

**Gamma**: Controls the contrast of the image.

**Middle Gray**: Indicates the middle gray value that will be preserved.


---
### Field Curvature DCTL
Applies an effect as if the lens has a strong field curvature, so the edges of the frame are out of focus, using a circular blur kernel with the ability to emulate cats eye in on the edges. Use this on a linear image. We strategically avoid sampling pixels that are not blurred, so the less blurry the image is, the faster this DCTL will run.

#### DCTL Parameters
**Protected Radius X/Y**: Choose what portion of the center of the frame is not blurred at all.

**Max Blur Strength**: Choose the maximum radius of the blur in the image, which will occur in the corners of the frame.

**Cats Eye**: Choose how much cats eye there will be in the blur at the edges. Higher is more cats eye and slightly faster playback performance

**Couple XY**: If checked, we substitute **Protected Radius Y** with your value entered for **Protected Radius X**

**Distort**: If checked, the cats eye will be computed in a way that more accurately reflects how cats eye perceptually distorts the blurred parts of the image. This happens because the center of the bokeh ball is not actually located on part of the frame that is responsible for it; the bokeh ball is cut from one side.

**Radius vs Strength Curve**: Shows you the blur radius used for different distances from the center of the frame, The x-axis represents location from the bottom left corner to the top right corner.

**Draw Blur Map**: Shows the blur radius for each pixel in the frame, scaled 0-1.

**Blur Falloff Function**: Controls how the blur strength maps from zero to **Max Blur Strength** as radius increases.

---

### Film Curve DCTL
Assumes the scene is a linear image, then converts to log10 exposure values, applies a sigmoid characteristic curve to get density, then computes transmittance. Parametric over each of the three channels.

In practice, you should use the following pipeline: `1. Clamp 0+ ==> 2. Film Curve (to simulate the negative) ==> 3. Color Gain ==> 4. Film Curve (to simulate the print) ==> 5. Gain (if you want white to not be 100%) ==> 6. Display Encoding`. (3) represents your printer lights and should make it so that middle gray is preserved at 0.18 from (1) to (4).

#### DCTL Parameters
**Red/Green/Blue Gamma**: Film gamma for each channel.

**Red/Green/Blue D_MIN**: Minimum density for each channel.

**Red/Green/Blue D_MAX**: Maximum density for each channel.

**Red/Green/Blue Offset**: indicates how far to the left to move each characteristic curve in the Density vs Log10 Exposure chart.

**Mid Gray**: Indicates the mid gray value in the input image.

**Exposure Gain**: Increase or decrease the incoming exposure.

**Linear to Exposure**: Check to apply the Exposure Gain to convert from scene illuminance to Exposure value

**Exposure to Log10 Exposure**: Check to apply a Log10 Function to the Exposure value

**Characteristic Curve**: Check to apply the Sigmoid that converts from Log10 Exposure to Density

**Density to Transmittance**: Check to convert computed Density to Transmittance.

**Draw Characteristic Curve**: Draws the characteristic curve on-screen. The fat line in the middle is Lux-Seconds = 0.0, each vertical line is 1.0 Log10 exposure. The horizontal lines represent density in 1.0 increments.

**Curve Type**: allows you to use Sigmoid of "Quadratic Sigmoid", which follows a similar shape but has a more a brupt rolloff.



---

### Film Grain DCTL
Creates a random noise, inspired by statistical film models. You'll need to pass in a linear image and use two of these DCTLs in a pipeline, one for the Neg stock and one for the print stock, as each one returns the Transmittance of the film stock.

#### DCTL Parameters
**D Max**: Maximum density

**D Min**: Minimum density of the film.

**Grains Per Pixel**: Should control the variance of the noise. More grains results in a finer image.

**Num Layers of Grains**: Should contribute towards controlling the gamma of the film. Essentially controls how thick the emulsion layer is.

**Activation Threshold**: Controls the amount of light needed for a grain to be activated.

**Photon Gain**: Exposure increase applied to the incoming light.

**Seed Position X/Y**: Indicates where in the image to pull a pixel to start the random seed. Change this if the noise is fixed.

**Noise Mode**: Indicates a different noise mode. In RGB, noise is computed on each channel independently, In Monochrome Noise mode, I recycle the same random seed for all three channels to avoid introducing chroma noise.

---
### Gain Normalization
**Note**: Just use the [Rebind LGGO DCTL](#rebind-lggo-dctl) below.

Make a sandwich of two of these DCTLs, with the first set to Reference White and the second set to Normalize White. Put linear gain in between, and the normalize white node will apply a global gain adjustment (exposure) to all three channels such that the mean or max of a (1, 1, 1) input to your linear gain adjustment is restored to 1.0.

#### DCTL Parameters
**Mode**: If set to Reference white, this replaces the top left pixel with a (1, 1, 1) chip. If set to Normalize, this reads that chip, computes a normalization, and then applies an exposure adjustment to bring the rendered chip to 1. Also clones over the chip so that it's not visible in your image anymore.

**Normalization**: Choose between Max or Mean to determine whether the max of the channels of the pixel in the corner is used, or the mean of its channels.


---

### Halation DCTL
DCTL that physically emulates film halation, intended for Linear input images.

#### How Halation works
Light passes through three layers of film emulsion and various color filters, ultimately with the bottom channel being Red. Light then passes through the film base and reflects off the back of the film, and this red light then re-exposes the channels in reverse order (red, then green, then blue).

#### DCTL Parameters

**Reflection exposure lost** (stops): As light passes through the film base and reflects off the anti-halation layer, it loses brightness. This parameter controls how many stops of light are lost by the time the reflection reaches the red channel again (as well as the other two channels) on the rebound. Use this slider to reduce or increase the overall amount of halation.

**Green exposure lost** (stops): Controls how much light is lost when the reflected light passes through the red channel and then exposes the green channel. This is added to the Reflection exposure lost.

**Blue exposure lost** (stops): Controls how much light is lost when the reflected light passes through the green channel and then exposes the blue channel. This is added to the Green exposure lost and the Reflection exposure lost.

**Blur Amount** (Thousandths of image width): The light reflection is blurry by virtue of being out of focus and by being diffused by the film base and anti-halation layer. This control represents the width/spread of the applied blur.

**Blur Type**: Choose which kernel to use when emulating the diffusion step.

**Red Shift Correction**: Because Halation re-exposes the red channel first, it will make the exposed negative more red than it originally was. This allows you to choose how you want to correct for this red tint. If you select Matrix, then it will fully correct, otherwise RGB Gain just corrects the white point and No Correction skips this step and leaves the red tint.




---
### Hue Curve DCTL
Hue rotation and hue variance adjustments to target a specific hue, much like a hue v hue curve.

#### Motivation
A common problem with Hue v Hue adjustments is that it's easy to rotate one hue past its neighbors. This DCTL attempts to address that by providing only adjustments that do not suffer from that flaw. It allows for hue rotations as well as hue v hue slope adjustments in such a way that no hue will be pushed past its neighboring hues (the hue v hue curve always has nonnegative slope), and it allows you to make adjustments to the complementary hue so that you have some chance of smoothness in your grade.

To use this DCTL, convert your image to HSV or spherical or the color model of your choice with Hue being scaled 0-1, then apply this DCTL and indicate which channel in the input image corresponds to the Hue dimension, and transform back to RGB after the DCTL.

#### DCTL Parameters
**Selected Hue**: The hue angle, in degrees, that you want to make an adjustment to. 0 is red.

**Adjustment Amount**: The strength and direction of the adjustment. In Hue Rotation control mode, this rotates the selected hue (specifically, the applied hue rotation is the selection, times 72 degrees). In Variation Control mode, this increases or decreases the slope of the curve for the selected hue (specifically, the new slope will be `1.0 + the adjustment amount`).

**Left/Right Feather**: Represents the distance left and right of the selected hue that will be affected by the adjustment. It's a different amount for each of the two modes, so just turn on "draw curve" or adjust these by eye.

**Draw Curve**: Check to draw the working hue v hue curve. the solid vertical line represents the selected hue, and the dashed line, if present, represents the complementary hue (selected hue + 180 degrees).

**Curve Type**: Indicate whether to target a single hue, or to make a similar adjustment to the complementary hue. You'll easily fail the gradient smoothness checker if this is set to Single Hue, just by the nature of hue v hue adjustments.

**Control Type**: Indicate whether you want to rotate the selected hue, or adjust the slope of the hue v hue curve at the selected hue.

**Channel**: Indicate which channel corresponds to hue in the input image.

---

### Lens Distortion DCTL
Applies a basic lens distortion model, uses bilinear sampling to avoid aliasing problems for reasonable choices of $k_1$ and $k_2$.

#### How it works
Lens distortion here is modelled with:
$r_d = \sqrt{x_d^2 + y_d^2}$
$x_u = x_d (1 + k_{1x} r_d^2 + k_{2x} r_d^4)$
$y_u = y_d (1 + k_{1y} r_d^2 + k_{2y} r_d^4)$

#### DCTL Parameters
**X Distortion Amount K1**: Chooses the value of $k_{1x}$ in the above model

**Y Distortion Amount K1**: Chooses the value of $k_{1y}$ in the above model

**X Distortion Amount K2**: Chooses the value of $k_{2x}$ in the above model

**Y Distortion Amount K2**: Chooses the value of $k_{2y}$ in the above model

**Couple XY**: If checked, just use the same $k_{1x}, k_{2x}$ for both $x_u$ and $y_u$ calculations, keeping the lens distortion spherical.

---
### Linear Contrast DCTL
Applies a power function to the RGB channels, keeping 0.18 unchanged. This DCTL expects a scene linear image.

#### How it works
The DCTL works in three steps:
1. Apply gain to shift Middle gray to 1.0
2. Raise the code values to the power of `Neutral Gamma * Color Gamma` if Ungroup RGB is checked, otherwise `Neutral Gamma`
3. Revert the gain done in step 1 (divide by that scaling rather than multiply)

#### DCTL Parameters
**Neutral Gamma**: Gamma applied to all channels

**Red Gamma**: Gamma to be applied only to the Red Channel

**Green Gamma**: Gamma to be applied only to the Green Channel

**Blue Gamma**: Gamma to be applied only to the Blue Channel

**Mid Gray**: Specifies the middle gray code value that is preserved.

---
### Matrix Manipulator
Provides an HSV-like user interface for 3x3 Matrix operations, analogous to adjusting the RGB chromaticity coordinates for a 3x3 Matrix. Apply this to a linear image. Aims to map a pure red, green, or blue input to a specific hue/saturation (but not value), and to map a pure white $(1, 1, 1)$ input to pure white output.

#### DCTL Parameters
**Red/Green/Blue Hue**: Indicate the HSV hue adjustment you you want to make to a pure Red/Green/Blue input. The angle specified here is added to the hue angle corresponding to a pure Red/Green/Blue input. Value not necessarily preserved.

**Red/Green/Blue Sat**: Indicate the HSV sat adjustment you you want to make to a pure Red/Green/Blue input. This is multiplied by the input saturation.

**Model**: Choose whether Hue and Saturation are computed in HSV or Cylindrical

**Invert**: Check to invert the matrix so you can use this in a sandwich.

---

### MTF Curve DCTL
Gives you control over a MTF-like curve. Internally makes passes of different frequencies which can be increased or reduced in gain before combining them back together. Highly recommend using the Quotient method and feeding this DCTL a log image.

#### DCTL Parameters
**Band 16-1:1 Contrast**: Applies a gain to the information captured only by this band. Set to 0 to soften the image and raise up to 2 to increase sharpness. The bands are relative to the timeline resolution, with a 16:1 blur, 8:1 blur, 4:1 blur, and 2:1 blur.

**Debug Band**: Specifies which band is viewed when the Debug Mode isn't None.

**Debug Mode**: This pull-down allows you to figure out what each band targets. You can choose from None (runs the plugin normally), Low Pass Mode (shows you the information that's too low frequency to be captured in this band), High Pass Mode (shows the information that's in this band), and High Pass Gray Mode (Same as High Pass mode, but normalized to 0.5 so that the frequency data in this band is more visible).

**Performance Mode**: Choose between Quality and Performance. Performance mode takes fewer samples when computing the blur which can cause very subtle artifacts, whereas Quality densely samples the region of the blur kernel.

**Method**: Allows you to choose between Quotient and Difference, which correspond to different ways to compute the frequency bands. In most real-world scenarios, the Quotient method provides better looking results, but the Difference method performs more accurately on zebra striped test charts. Here's the math:
```
quotient_out := (input_value / low_pass5)^band5_contrast * (low_pass5 / low_pass4)^band4_contrast * ... * low_pass1
difference_out := (input_value - low_pass5)*band5_contrast + (low_pass5 - low_pass4)*band4_contrast + ... + low_pass1
```


---
### Parametric Blur DCTL
Blur kernel where you can choose the Distance vs Weight function. Use this on a linear image.

#### DCTL Parameters
**Falloff Start**: Distance to Blur Radius that should be assigned weight 1.0.

**Falloff Gamma**: Adjusts the curvature of the spread function.

**Blur Radius**: Adjusts the radius of the blur kernel. This is normalized to a 2048 pixel wide frame so that when you change timeline resolution, the appearance of the blur should remain unchanged.

**Blur Opacity**: Adjust the opacity of the blur. If you want to emulate a diffusion filter, set this to around 0.2.

**Draw Curve**: Shows you the distance vs weight function of the kernel. The dashed line in the middle represents the center of the kernel, and the dashed lines on the left and right side represent a distance equal to **blur radius**. The curve represents the weight assigned at each distance. Under the hood, the area under the curve is normalized to equal 1.0.


---

### Photon Noise DCTL
Helps simulate the effect of photon noise, a noise that's approximately poisson distributed, where the variance is proportional to the intensity of the signal. Apply this to a linear image.

#### DCTL Parameters
**Photon Exposure** (stops): The input signal is multiplied by `_exp2f(photon exposure)`to compute the variance

**Noise Mode**: Indicates a different noise mode. In RGB, noise is computed on each channel independently, In Monochrome Noise mode, I recycle the same random seed for all three channels to avoid introducing chroma noise.

**Seed Position X/Y**: Coordinate of the pixel used to generate a random seed.




---

### Random Channel Mixer
Constructs a random RGB matrix that is some distance away from the Identity matrix. Useful when trying out lots of different looks, expects image to be converted to Linear before using.

#### DCTL Parameters
**Eps**: Maximum acceptable entry-delta from the identity matrix. Essentially controls the intensity of the applied effect. In some cases, a value about 0.33 will result in division by zero errors and numerical instability when rows are rescaled.

**Seed**: Indicates the random seed used to construct the matrix. Handy if you want to remember the value for later and reproduce a certain look.

**Maintain White**: If checked, scales each row of the RGB matrix to each sum to 1. This helps keep grays neutral in the final result. If unchecked, the image can take on a tint, with luminance maintained by scaling the entire matrix to sum to 3 (but individual rows can sum to values other than 1).

**Show Matrix** [OFF, FLOAT VALUE, SCALED TEN BIT VALUE]: If set to "Float Value", the entries of the matrix are displayed, allowing you to copy the values down using the RGB picker in Fusion. If set to "Scaled Ten Bit Value", the entries of the matrix are displayed, and if you have a 10-bit color picker, the difference between the code value and 500 represents the hundreths of a point that you should enter in the corresponding entry in the RGB Mixer. IE if the top middle patch has a 10-bit code value of `496`, you would enter `-0.04` for the Green channel in the Red Output section of the RGB Mixer.




---

### Random Contrast Curve
Constructs a contrast curve, has the option to procedurally generate one with random parameters so you can try lots of different curves in a moment.

#### DCTL Parameters
**Pivot**: Specify the pivot point, which will remain unchanged in color and value.

**Toe**: Indicates what distance from the pivot to start rolling off the shadows. 0.0 is at the pivot point, 1.0 is near the black point.

**Shoulder**: Indicates what distance from the pivot to start rolling off the highlights. 0.0 is at the pivot point, 1.0 is near the white point.

**Black Point**: Specifies the minimum value in the image.

**White Point**: Specifies the maximum value in the image.

**Pivot Slope**: Specifies the slope of the curve when measured at the pivot point.

**Seed**: Random seed, only used if Randomize box is checked.

**Show Curve**: Check this box to get a graphical display of the curve. Within the gridded area, the x-axis goes from 0.0 to 1.0, negative values are shown to the left and right of the display.

**Randomize**: Check this box to randomly select parameters for the curve (excluding pivot).

**Ungroup RGB**: When checked, if Randomize is also checked, then this will randomize a contrast curve for each of the RGB channels.



---

### Random Linear Contrast
Expects a linear image, applies linear contrast to each channel via gamma, preserving mid gray, but you can use a random number generator so you can try a lot of different curves in only moments.

#### DCTL Parameters
**Global Contrast**: Initial gamma applied to all channels.

**Red/Green/Blue Contrast**: Gamma added to Global gamma for the corresponding channel.

**Random Interval**: Maximum amount that a randomly selected gamma can deviate from a per-channel gamma or the global gamma

**Random Seed**: User selected seed for the random number generator.

**Mid Gray**: Linear value of mid gray.

**Use Random**: Choose whether to not use the random number generator, to randomly generate a split tone (randomness is applied only to the per-channel contrasts), to randomly augment the Global Contrast, or both.




---

### RGB Linear Contrast DCTL

**(Deprecated - Use "Linear Contrast DCTL" instead.)**

You can find the old version of this DCTL [here](https://github.com/thatcherfreeman/utility-dctls/blob/167d849241ddd1e6dbd3963e2be3601694173a38/Effects/RGB%20Linear%20Contrast.dctl)

Applies a power function to the RGB channels, keeping 0.18 unchanged. This DCTL expects a scene linear image.

#### How it works
The DCTL works in three steps:
1. Apply gain to shift Middle gray to 1.0
2. Raise the code values to the power of `Neutral Gamma * Color Gamma` if Ungroup RGB is checked, otherwise `Neutral Gamma`
3. Revert the gain done in step 1 (divide by that scaling rather than multiply)

#### DCTL Parameters
**Red Gamma**: Gamma to be applied only to the Red Channel (if Ungroup RGB is checked)

**Green Gamma**: Gamma to be applied only to the Green Channel (if Ungroup RGB is checked)

**Blue Gamma**: Gamma to be applied only to the Blue Channel (if Ungroup RGB is checked)

**Neutral Gamma**: Gamma applied to all channels, regardless of Ungroup RGB

**Mid Gray**: Specifies the middle gray code value.

**Ungroup RGB**: If unchecked, only applies the Neutral Gamma, otherwise applies both Neutral gamma and the Color Gamma, multiplying together those two powers.




---

### Subtractive Saturation DCTL
Computes saturation in a way that adds "density" to more saturated colors, making them darker. Expects a Linear image.

#### How it works
Suppose a pixel is a color `input`. The DCTL will first compute a `Value` (IE luminance) of that pixel using one of many methods, and from there it can compute the input's `Color` by taking `input / Value`. The color is saturated or desaturated using the Gamma controls (we raise each channel of the `Color` to a power). From there, we multiply the `Color` by a different luminance called `Density` that's calculated using the method specified by the second dropdown menu. The result is scaled so that white is preserved.

#### DCTL Parameters
**Color Gamma**: Controls the saturation of the image.

**Cyan Gamma**: Saturation slider that's combined with the Color Gamma slider, moving this to the right will make the image more cyan.

**Magenta Gamma**: Similar to Cyan Gamma slider.

**Yellow Gamma**: Similar to Cyan Gamma slider.

**Density**: Allows you to control how much density is added, on a scale of 0 (`Density` is computed using the same method as `Value`), to 1 (`Density` is computed using the specified method). The floating scale effectively lets you choose the strength of the specified method.

**Value Calculation**: Allows you to select how the `Value` is computed. I don't recommend the Max or Min methods, and you should generally choose a method that runs large (Arithmetic Mean, Geometric Mean, and L2 Norm are recommended).

**Density Calculation**: Allows you to choose how the `Density` is computed. Again, I don't recommend the Max or Min methods, and you should choose a method that runs small (Harmonic Mean is recommended.)




---

### Tone Mapping DCTL
Applies a sigmoid function to compress highlights. Attempts to target a specific black point, white point, mid_gray, and slope at mid gray. Expects a linear state image and outputs a linear state image.

#### How it works
The DCTL computes the $h(x)$, where: $h(x) = g(m_i(x/m_i)^\gamma)$ and $g(x) = a\frac{x}{x+b} + c$. The parameters $a, b, c, \gamma$ are selected for you based on the specified white point, black point, and target slope, and input/output mid gray points.

#### DCTL Parameters
**Target Slope**: Linear slope at the output mid gray. $\gamma$ is selected so that $h'(m) = \text{target slope}$.

**White Point**: Maximum output, typically 1.0 corresponds to 100 nits, and $h(x)$ will asymptotically approach this value as $x \rightarrow \infty$.

**Black Point**: This indicates where $h(0)$ will map to. If your linear image has negative code values, they can map to be below this black point.

**Input Mid Gray**: Indicate the value corresponding to $m_i$.

**Output Mid Gray**: Specifies the value corresponding to $m_o$. We choose gamma such that $h(m_i) = m_o$.

**Scale Mid Gray with White Point**: If checked, the value of $m_o$ is overridden to `output_mid_gray * (white_point - black_point) + black_point`. If unchecked, $m_o$ is just set equal to `output_mid_gray`. If you want your mid gray to scale with the max output white point as you change white points, then check this box.



---

### Vignette DCTL
Corrects for a vignette in the image, only handles circular vignettes for now, expects a scene linear image.

#### DCTL Parameters
**Vignette Amount**: Uses a model of `1 + ar^2` to determine the amount of vignetting, then multiplies to vignette the image. Vignette amount controls the value of `a`.

**Show Vignette**: If checked, outputs the image that is multiplied by the source image.




## Operations



---

### Addition Function DCTL
Adds a value to each channel. The channels are computed by $\text{Red}_{\text{out}} = \text{Red}_{\text{in}} + \text{Global Offset} + \text{Red Offset}$ and likewise for the other two channels.




---

### Clamp DCTL
Clamps the code values of the current frame to the specified Min and Max values, such that for any `x`, we will then have `clamp_min <= x <= clamp_max`

#### DCTL Parameters
**Min Clamp**: Specifies the value at which we will set `x = max(x, Min Clamp)`

**Max Clamp**: Specifies the value at which we will set `x = min(x, Max Clamp)`

**Clamp Min (Checkbox)**: Uncheck to bypass the Min Clamping step.

**Clamp Max (Checkbox)**: Uncheck to bypass the Max Clamping step.




---

### Color Generator DCTL
Generates the specified RGB value across the whole frame. Also allows you to bypass certain channels via the "Pass-through" checkboxes.

#### DCTL Parameters
**Red/Green/Blue**: the Red/Green/Blue value that will be returned.

**Red/Green/Blue Pass-Through**: If checked, just return the red/green/blue value of the input image.


---

### Color Sampler DCTL
Samples the pixel at the specified coordinate, then fills the frame with the sampled color.

#### DCTL Parameters
**Sample X/Y**: X/Y coordinates to sample from

**Window Size px**: We sample a square region of this width in pixels around the selected x,y coordinate and sample the pixels in the window.

**Mode**: Choose "Crosshair" to see which pixels you're sampling (located at the intersection of the two lines) and choose "Sampled Color" for the sampled color to be displayed across the whole frame.


---

### Cross Product DCTL
Computes the cross product of the current color and the specified vector, or the cross product of the specified vector and the current color if you set the direction to $\overrightarrow{Vec} \times \overrightarrow{\text{Input RGB}}$.


---

### Dot Product DCTL
Takes the dot product of the current color and the specified `(r, g, b)` value.



---

### Gamma Function DCTL
Applies a power function with the reciprocal of the specified exponent.

#### DCTL Parameters
**Gamma**: Given some number $\gamma$, raise each of the RGB components to the power of $\gamma$

**Use Reciprocal**: If checked, instead raises each RGB component to the power of $1 / \gamma$.

**Negative Values**: For a negative input color component $x$, choose from:
* Clip 0 - returns $y = 0$
* y=x - Returns $y = x$
* y=x/gamma - Returns $y = x / \gamma$ so the slope somewhat scales according to the choice of exponent.
* Positive Reflection - Returns $y = \lvert x \rvert^\gamma$
* Sign Match Reflection - Returns $y = -\lvert x \rvert^\gamma$, returning a negative result if $x$ is negative.




---

### Invert DCTL
Inverts the values in an image.

#### DCTL Parameters
**Log Mode**: When checked, computes the inverse by taking `1 - x`. When unchecked, assumes the image is scene linear and therefore computes `1 / x`.





---

### Log Function
For each pixel and channel, takes the logarithm.

#### DCTL Parameters
**Log Base**: The base of the logarithm, 10.0 by default.

---
### Luminance Qualifier
Expects a scene linear image, generates a mask of pixels for which the selected channel is above or below some quantity of stops above/below middle grey.

#### DCTL Parameters
**Threshold**: Indicate the number of stops above mid grey you want the mask cutoff to take place at.

**Feathering**: Indicate the number of stops between 0% mask and 100% mask

**Mid Grey**: Indicate the value of mid grey

**Center Feathering at Thr.**: Indicate whether the threshold is mapped to 100% in the mask (if unchecked) or to 50% in the mask, if checked.

**Selection**: Choose Select Shadows for values between 0 and threshold to be selected, and choose "Select Highlights" to select between the threshold and Infinity.

**Channel**: Select which number is compared to the threshold to compute the mask. Luminance uses Rec709 Luminance coefficients.


---

### Matrix
Multiplies the RGB values of the input by a 3x3 matrix with the specified entries. Supports negative values. Given your input $x = [r, g, b]^T$, this computes $f(x) = Ax$. If you choose to preserve neutrals, then we will ensure that the rows of $A$ sum to 1.0, so please make sure the matrix doesn't have rows of zeros if you intend to use that feature.

#### DCTL Parameters
**Red/Green/Blue => Red/Green/Blue**: Indicates the coefficient corresponding to how much of the left hand side (input) channel will be included in the right hand side channel (output). The entries ending with "=> Red" are the first row of the matrix, the entries ending in "=> Green" are the second row, etc.

**Preserve Neutral**: Sends $(1, 1, 1)$ through the matrix and applies RGB gain to the output to ensure that $(1, 1, 1)$ is ultimately returned.

**Invert**: computes the inverse of the matrix and then applies it.


---

### Modulo Function DCTL
Takes the input $x$ and computes $x \mod y$, the remainder when dividing $x$ by $y$.

#### DCTL Parameters
**Global Denominator**: If Use Per-Channel Denominator is unchecked, then the modulo of all three channels is computed with respect to this number.

**Red/Green/Blue Denominator**: If Use Per-Channel Denominator is checked, then each channel's modulo will be computed with respect to the corresponding number.

**Use Per-Channel Denominator**: Check in order to compute modulo with a different denominator for each channel.




---

### Multiplication Function DCTL
Multiplies each channel by a value. The channels are computed by $\text{Red}_{\text{out}} = \text{Red}_{\text{in}} * \text{Global Gain} + \text{Red Gain}$ and likewise for the other two channels.



---

### Polynomial Kernel DCTL
For each of $x_i \in \{r, g, b\}$, computes $(x_i \cdot x_j)^p$ and allows you to specify a linear combination of those into each of the r, g, b channels

#### How it works
One of the tricks with SVMs is the Polynomial kernel, where you extend your feature vector with $k(x_i, x_j) = (x_i * x_j)^p$ for some integer $p$, and for all $x_i$ or $x_j$ in your original input feature vector. This results in a higher dimensional input (in this case, 9 unique dimensions) where the dimensions are as follows: $r, g, b, k(r, r), k(g, g), k(b, b), k(r, g), k(r, b), k(g, b)$

Now, we can convert back to 3 dimensions by multiplying by a $3 \times 9$ matrix, which you specify with the parameters. I've intentionally actually skipped most of the first three columns as you can figure those out yourself with a normal 3x3 matrix prior to this DCTL, and that keeps it way cleaner.

There's an interesting special case when $p = 0.5$ and you're therefore taking the geometric mean of each pair of channels, and effectively get a 3x3 matrix in here too.

#### DCTL Parameters
**Red/Green/Blue => Red/Green/Blue**: The coefficient corresponding to the original color.

**Red/Green/Blue * Red/Green/Blue => Red/Green/Blue**: The coefficient corresponding to this $(x_i \cdot x_j)^p$ term.

**Power**: The value of $p$.

**Mid Gray**: Indicates the code value for Mid Gray, that will be restored via RGB gain if Preserve Gray is checked.

**Identity Point for Products**: By default, $x^p$ obviously is an identity function only when $x = 1$ (or $x = 0$). This allows you to choose a different stationary point, as we will scale the input and output of the power such that $x$ remains stationary for this specified value when Normalize Powers is checked.

**Preserve Gray**: If checked, runs mid-gray through the pipeline and applies gain at the end to restore it.

**Normalize Powers**: If checked, powers will be normalized at the value specified by Identity Point for Products.



---

### Power Function DCTL
Computes the function $\texttt{base}^x$.

#### DCTL Parameters
**Base** The base of the exponent, raised to the power of the input pixel.


---

### Projective Transformation Matrix DCTL
Rather than applying a 3x3 matrix, we can apply a Projective Transform.

#### How it works
Traditionally, you'd make a matrix $M_1 \in \mathbb{R}^{3 \times 3}$ and apply the matrix multiply:
```math
\begin{bmatrix} r' \\ g' \\ b'\end{bmatrix} = M_1 \begin{bmatrix} r \\ g \\ b \end{bmatrix}
```

Frequently used in computer graphics, there's a slightly more expressive alternative called Projective Transforms that make use of homogeneous coordinates. You would instead have $M_2 \in \mathbb{R}^{4 \times 4}$ and make the following modifications:

```math
\begin{bmatrix} r' \\ g' \\ b' \\ c' \end{bmatrix} = M_2 \begin{bmatrix} r \\ g \\ b \\ 1.0 \end{bmatrix}
```

You'd then output the color:

```math
\begin{bmatrix} r'/c' \\ g'/c' \\ b'/c' \end{bmatrix}
```

You can see that this is strictly more expressive than the $3 \times 3$ matrix approach because you could define $M_2$ in the following way:

```math
M_2 = \begin{bmatrix} M & 0 \\ 0 & 1 \end{bmatrix}
```

This DCTL allows you to construct $M_2$.

#### DCTL Parameters

**Red/Green/Blue/Bias => Red/Green/Blue/Bias**: These are listed in the same order as if you were reading $M_2$ row by row. Almost all the interesting behavior happens in the fourth row.

**Preserve Neutral**: If checked, applies an RGB gain operation at the end that restores white inputs to (1.0, 1.0, 1.0).

**Linearize White**: If checked, applies a curve to make the grayscale ramp a straight line.


---
### Root Polynomial Degree 2 DCTL
Applies a $3 \times 6$ matrix $A$ in the following way:

```math
A \begin{bmatrix} R \\ G \\ B \\ \sqrt{R * G} \\ \sqrt{R * B} \\ \sqrt{G * B} \end{bmatrix}
```

You can fit this matrix with my tool in my [rgb-matrix-finder](https://github.com/thatcherfreeman/rgb-matrix-finder) repo.

#### DCTL Parameters
**Mat 00-25**: First digit is the row, second digit is the column of the matrix.

---
### Scaled Gamut DCTL
Scales your selected black point and white point to the 0-1 range, essentially a gain+offset adjustment. Useful if you want to work in some log space that has a nonzero black point. Just measure the black point and white point of your working log curve (say, using a shot of a lens cap or just sending black or white through a lin to log conversion), enter those values and copy/paste the dctl to sandwich your LGGO primaries adjustments, in the latter one checking invert.

#### DCTL Parameters
**Black Point**: Indicate what value should be mapped down to 0.0.

**White Point**: Indicate what value should be mapped to 1.0.

**Invert**: Inverts the adjustment, so 0.0 is mapped to **Black Point** and 1.0 is mapped to **White Point**.

---

### Sigmoid Function DCTL
Applies the sigmoid function to the inputs. Computes $b + (w-b)\frac{1}{1 + e^{-c(x-d)}}$.

#### DCTL Parameters
**X Midpoint**: Controls the value of $d$. Vanilla sigmoid has this set to 0.0.

**Contrast**: Controls the value of $c$. Vanilla sigmoid has this set to 1.0.

**Output White**: Controls the value of $w$. Vanilla sigmoid has this set to 1.0.

**Output Black**: Controls the value of $b$. Vanilla sigmoid has this set to 1.0.



---

### Sigmoid Kernel DCTL
Similar to Polynomial Kernele. For each of $x_i \in \{r, g, b\}$, computes $\sigma((x_i \cdot x_j)^p)$ where $\sigma(x) = \frac{x}{x + w}$, with $w$ being a user specified white point. Allows you to specify a linear combination of those into each of the r, g, b channels. You should use a linear input for this function.

#### How it works
One of the tricks with SVMs is the Polynomial kernel, where you extend your feature vector with $k(x_i, x_j) = \sigma((x_i * x_j)^p)$ for some integer $p$, and for all $x_i$ or $x_j$ in your original input feature vector. This results in a higher dimensional input (in this case, 9 unique dimensions) where the dimensions are as follows: $r, g, b, k(r, r), k(g, g), k(b, b), k(r, g), k(r, b), k(g, b)$

Now, we can convert back to 3 dimensions by multiplying by a $3 \times 9$ matrix, which you specify with the parameters. I've intentionally actually skipped most of the first three columns as you can figure those out yourself with a normal 3x3 matrix prior to this DCTL, and that keeps it way cleaner.

#### DCTL Parameters
**Red/Green/Blue => Red/Green/Blue**: The coefficient corresponding to the original color.

**Red/Green/Blue * Red/Green/Blue => Red/Green/Blue**: The coefficient corresponding to this $\sigma((x_i \cdot x_j)^p)$ term.

**Power**: The value of $p$.

**Mid Gray**: Indicates the code value for Mid Gray, that will be restored via RGB gain if Preserve Gray is checked.

**White Point**: The value of $w$ in the denominator of $\sigma(x)$.

**Preserve Gray**: If checked, runs mid-gray through the pipeline and applies gain at the end to restore it.




---

### Softmax DCTL
Applies a Softmax function, with Temperature. Outputs in the 0-1 range for all real inputs.

#### DCTL Parameters
**Temperature**: Scales the input values, so larger values will result in a more extreme output.



---

### Tanh Function DCTL
Computes a tanh of the input via $g \tanh(c (x - b))$.

#### DCTL Parameters
**Horizontal Offset**: Controls the value of $b$. Vanilla tanh has this set to 0.0.

**Contrast**: Controls the value of $c$. Vanilla tanh has this set to 1.0.

**Output White**: Controls the value of $g$. Vanilla tanh has this set to 1.0.

**Maintain Contrast**: If checked, then the Contrast control controls the derivative at x=0 even if the output white is changed (IE $c$ is scaled by $1/g$).



---

### Unit Length DCTL
Takes the current `(r, g, b)` color value, computes the L2 norm, and divides each component by the norm to convert the vector to unit length.


---

### Vector Norm DCTL
Computes various norms of the given vector.

#### DCTL Parameters
**Norm Type**: Choose between `L1 Norm, L2 Norm, Lp Norm, Maximum, Minimum, Arithmetic Mean, Geometric Mean, Harmonic Mean` to choose the norm type.

**P-Norm Power**: If `Lp Norm` is selected for the norm type, this selects the value of `p`. Lp norm is computed by $(\lvert r \rvert^p + \lvert g \rvert^p + \lvert b \rvert^p)^{1/p}$, and L1 and L2 norm are special cases of this.



## Utilities



---

### ACES Exposure DCTL
DCTL that allows for adjustment of exposure in ACES. Important: It's probably better to just set your timeline color space to the ACES color space you want to use, and then to use the Exposure slider in the HDR color wheels.

#### How it works
Internally, this DCTL converts ACEScc or ACEScct to Linear, and then applies a gain according to the specified exposure adjustment before converting the image back into the original color space.

#### DCTL Parameters
**ACES Gamma**: Pulldown menu in which you select from ACES (Linear), ACEScc, and ACEScct. This is where you specify the gamma of the image that is being fed into this DCTL.

**Exposure Adjustment**: Specifies the number of stops to increase or decrease (negative) exposure.



---

### Bit Depth Estimator DCTL
Tool to help estimate the true bit depth of a file. It works by comparing the code values in the current pixel to the adjacent pixels and measuring the smallest nonzero difference between the corresponding channels to estimate the effective bit depth for the current pixel.

#### DCTL Parameters
**Target Bit Depth**: When Highlight is enabled, Highlights all pixels whose effective bit depth is within 0.1 of this Target Bit Depth.

**Highlight**: When checked, highlights only pixels whose bit depth is near the Target Bit Depth, otherwise all pixels are replaced with their effective bit depth.




---

### Blanking Checker DCTL
Helps you spot pixels with NaN, infinity, negative, zero, or superwhite channels. Pixels with certain conditions are replaced by a specified highlight color. Optionally, the highlight can be a checkerboard shape.

#### DCTL Parameters
**Highlight Color Red**: Red component of the highlight color.

**Highlight Color Green**: Green component of the highlight color.

**Highlight Color Blue**: Blue component of the highlight color.

**Checkerboard Size**: Square size of the generated checkerboard, if set to zero, just uses the Highlight Color.

**Lower Bound**: Indicates the lower bound used as a comparison point for some of the below sliders.

**Upper Bound**: Indicates the upper bound used as a comparison point for some of the below sliders

**Highlight NaNs**: Highlights pixels with a NaN channel.

**Highlight -Inf**: Highlights pixels with -infinity as at least one channel

**Highlight < Lower**: Highlights pixels with values less than the specified lower bound.

**Highlight == Lower**: Highlights pixels that have a channel equal to the specified lower bound.

**Highlight == Upper**: Highlights pixels that have a channel equal to the specified upper bound.

**Highlight > Upper**: Highlights pixels that have a channel that exceeds the specified upper bound.

**Highlight +Inf**: Highlights pixels with +infinity as at least one channel.


---

### Brand Colors DCTL
Helps you check if you hit the code values required/provided by some brand. Throw this at the very end of your pipeline (after the ODT) and enter the RGB values that the brand expects in the Target Color section. Then, this tool will highlight when code values that are close to the specified color exist in the image.

#### DCTL Parameters
**Interval Range %**: Specify what percent difference between the current pixel and the target color will result in a highlight. IE we compute:
```c
low_bound  = target_rgb * (1.0 - (percent_error / 100.0))
high_bound = target_rgb * (1.0 + (percent_error / 100.0))
```

**Highlight Red/Green/Blue**: If all three channels of the current pixel lie between `low_bound` and `high_bound`, then the pixel will be colored according to this specified Highlight color.

**Highlight Opacity**: Indicates how opaque the highlighting color is.

**Target Color Red/Green/Blue**: Specify the code value of the target color. This can be done on a 0-1 scale, or a 0-255 8-bit scale.

**Target RGB Format**: Indicate whether the target color is specified on a 0-1 scale, or a 0-255 scale.

**Highlight Mode**: Choose whether to Generate the Target Color or to highlight pixels that fall within or outside the interval centered on the target RGB.

---

### Channel Viewer DCTL
Emulates the Fusion channel viewer, for Red/Green/Blue channels.

#### DCTL Parameters
**Channel**: Allows you to choose whether the full color image will be returned, or only one of the red/green/blue channels (duplicated onto all three channels in the output for visibility).


---
### Chroma Subsampling Chart DCTL
Chart to help you identify chroma subsampling issues by drawing one-pixel wide stripes every third row or column of pixels. If you have smearing between rows, then you know that the chroma vertical resolution is not full (the third digit in 4:4:4 is either 2 or 0). If you have smearing between columns, then you know the chroma horizontal resolution is not 4, so the second digit is either 2 or 1. Compare the GUI viewer with your external monitor and try applying the below Chroma Subsampling DCTL in the GUI for a low fidelity simulation of each kind of chroma subsampling.

---

### Chroma Subsampling DCTL
Applies chroma subsampling to an image by converting to YCbCr, downsampling the Cb and Cr channels via box averaging, then converting back to RGB.

#### DCTL Parameters
**X/Y Offset**: Allows you to offset the 2x4 filter box.

**Convert to YCbCr**: Check this box to return the YCbCr image instead of converting back to rec709.

**Chroma Subsampling Type**: Allows you to choose which kind of chroma subsampling to use.


---
### CIELUV DCTL
Converts between XYZ and CIELUV, CIELCH, or CIELSH.

#### DCTL Parameters
**White Point x,y**: Indicates the xy chromaticity coordinates of the white point. D65 by default.

**White Point Luminance**: Indicates nits of luminance for the white point.


---

### ColorChecker DCTL
Generates a synthetic image of the Macbeth ColorChecker based on one of two datasets: the X-Rite post-2014 measured LAB values, or the original paper (you can find in Documentation/ColorChecker.pdf). Outputs in XYZ/Linear color space.

#### DCTL Parameters
**Exposure Adjustment**: Stops of exposure adjustment, in case the rendered image isn't your preferred brightness.

**Outer Border Width**: How much black border to draw around the whole image.

**Inner Border Width**: How much black border to draw around individual chips.

**Dataset**: Choose Official to use the X-Rite values, and use McCamy to use the one from the old paper and wikipedia.

**Adapt to D65**: Check this box to use a bradford chromatic adaptation matrix to best approximate what the chart would look like under a D65 illuminant. Leave unchecked to use the native white point for each dataset (Illuminant A for official, Illuminant C for McCamy).

---
### Color Picker DCTL

Improves upon the color picker in the Color page by allowing you to see floating point code values that aren't clamped 0 to 1.

#### DCTL Parameters
**Color Picker X/Y**: Coordinates of the pixel you want to sample.

**Sample Size px**: Size of the window of pixels you'd like to average. When this is 1, we only sample a single pixel.

**Num Digits**: Number of digits to show in the legend.

**Format**: Indicate whether to show floating point or integer values of a given bit depth.

**Crosshair Type**: Indicate the shape of the crosshair, in case the large + is too distracting.

**Legend Position**: Specify where you want the legend to be placed.

**Legend Color**: Specify whether you want the text and crosshair to be White, black, gray, or the inverse of the underlying color.

---

### Color Ramp DCTL
Creates a color ramp from 0 to 100% Hue, Saturation, or Luminance. This can be used to monitor the output of your tools and overall node pipeline.

#### DCTL Parameters
**Ramp Type**: Choose from Luminance, Saturation, or Hue ramp.

**Saturation Ramp Hue**: If Saturation ramp is selected, then this controls the hue of the ramp.

**Hue Ramp Saturation**: If Hue ramp is selected, then this controls the saturation of the hue ramp.



---

### Cube Rotate DCTL
Takes the specified vector and rotates the RGB cube (around 0,0,0) so that the given vector is now achromatic.

#### DCTL Parameters
**Color R, Color G, Color B**: The RGB components of the vector that will be rotated gray.

**Inverse**: Rotates the cube the opposite angle, so that the currently white vector rotates to the direction of the specified vector, therefore doing the opposite of the normal version.

---

### Cylindrical DCTL
Converts between RGB and a Cylindrical color model. Outputs a 3-channel image, $(\theta, \phi \rho)$. $\rho$ represents `mean(rgb)`, $\theta$ is scaled 0-1 and represents the hue, and $\phi$ represents saturation and is scaled from 0 to 1.0 for inputs that are all nonnegative.

#### DCTL Parameters
**Direction**: Indicate whether to go from RGB to Cylindrical, or from Cylindrical to RGB.

---

### DaVinci LGGO DCTL
Recreation of DaVinci Resolve's Lift Gamma Gain Offset controls in the primaries, for reference for other developers. Recreates the global LGGO controls when lum mix is set to zero.

#### DCTL Parameters
**Lift/Gamma/Gain/Offset**: Recreation of the corresponding controls in the Primaries panel.

**Invert**: Inverts the adjustment made by these controls.

---

### DaVinci Tone Mapping DCTL
Recreation of the DaVinci Tone Mapping setting in the Color Space Transform effect. Expects a linear image and outputs a linear image. Currently only replicates the tone mapping when Adaptation is set to 9.

#### How it works
DaVinci Tone Mapping is simply a function of $f(x) = a \frac{x}{x + b}$, with some strategically selected $a$ and $b$ depending on your selected parameters. I've solved both $a$ and $b$ when Adaptation is set to 9.

#### DCTL Parameters
**Max Input Nits**: Quantity of nits that will be mapped to the Max Output Nits. Resolve is scaled so that linear 1.0 means 100 nits.

**Max Output Nits**: Max Linear value that will be in the output image.

**Adaptation**: Makes the image brighter or darker.

**User Input B**: When "Use Custom Adaptation" is checked, we use this value of $b$ instead of the one computed by default when Adaptation is 9. You'll have to use this if you want to emulate DaVinci Tone Mapping in the scenario that Adaptation is not equal to 9.

**Use Custom Adaptation**: Allows you to override the selection of $b$ when checked. Otherwise, $b$ is computed from the specified value of Adaptation.

**Invert**: Inverts the tone mapping with the specified parameters.

**Clamp**: Allows you to disable white point clamping. Resolve would have this permanently enabled.



---

### Exposure Chart DCTL
Creates a middle gray exposure chart, an exponential ramp, a linear ramp, and several gray exposure chips that are an integer number of stops above and below middle gray. This is intended to be used in a linear gamma timeline.

#### DCTL Parameters
**Number of Steps**: Specifies the number of exposure chips to be displayed in the chart. One of the ones in the middle will share its value with middle gray, and each chip to the right will have a code value double of the previous chip.

**Middle Gray Value**: Specifies the desired value of middle gray, which is 18% by default. This controls the brightness of the large chip in the middle too.

**Show Mid Gray Card**: Toggle to turn off the grey card in the middle.

**Show Linear Ramp**: Toggle to turn off the 0-1 scale ramp at the bottom.

**Show Exponential Ramp**: Toggle to turn off the smooth stop ramp at the bottom.

---

### False Color Generator DCTL
Generates a false color conversion for linear, computer generated images (not authorized for use in real photography). Allows you to assign colors to specific regions of the image, in one-stop increments. You set a black point, a shadow point, mid gray, a highlight point, and a white point, and you can assign colors to all regions between and outside of those bounds.

#### How to use
1. Load in a linear image
2. Apply this DCTL
3. Set the clipping point CV to the clipping point of the linear image.
4. Set the shadow/highlight stops to the points you feel appropriate
5. Set the Black cutoff where the black point is in your clip.
6. Convert this pipeline into a LUT.

#### DCTL Parameters

**Black Hue Angle**: Hue of colors below the Black Cutoff

**Near Black Hue Angle**: Hue of colors between Black Cutoff and Shadow Stop

**Shadow Hue Angle**: Hue of colors between shadow stop and mid gray

**Highlight Hue Angle**: Hue of colors between mid gray and Highlight Stop

**Near white Hue Angle**: Hue of colors between Highlight Stop and White Cutoff

**White Hue Angle**: Hue of colors brighter than the White Cutoff point

**Clipped Hue Angle**: Hue of colors whose Value exceeds the Clipping Point CV.

**Black Cutoff Stop**: Number of stops below middle gray below which we'll consider Black.

**Shadow Stops**: Number of stops below middle gray we'll color with the Shadow Hue Angle

**Highlight Stops**: Number of stops above middle gray we'll color the Highlight Hue Angle

**White Stops**: Number of stops above middle grey which we'll color with the White Hue Angle

**Clipping Point CV**: Linear code value for which if any channel exceeds this value, we will highlight it with the Clipped Hue Angle

**Middle Gray Value**: Indicates the Linear value we consider to be middle gray.

**Log Stops**: If "Log Output" is checked, controls the colorfulness and contrast of the output image.

**Clip to White**: Check this box to render Clipped values as white instead of as whatever hue was selected.

**Log Output**: Check this box if this DCTL isn't going into another CST that converts to a display or log color space.

**Disable Blacks/Near Blacks/Shadows/Gray/Highlights/Near Whites/Whites/Clipping**: Bypasses a specific set of colors.

**Brightness Mode**: If Luminance, then we simply take a weighted average of the RGB channels. If Value, then we take the channel with the maximum value before comparing it to any of the cutoffs or mid gray.

---

### Grid Chart DCTL
Draws a grid or a grid of dots so you can see how the [Field Curvature DCTL](#field-curvature-dctl) behaves. Or to photograph with your real lenses and see how their cats eye looks.

#### DCTL Parameters
**Number of Grids**: Amount of boxes to put on the X-axis.

**Grid Thickness Px**: Thickness of the lines in the grid or dots, in pixels

**Invert**: Invert the color of the chart so it's black lines on a white backdrop.

**Chart Type**: Choose whether to draw the grid or to draw dots.

---
### Frequency Test Chart DCTL
Draws radial or vertical bars at the specified frequency. Code adapted from Thomas Berglund

#### DCTL Parameters
**Frequency Start/End**: Specifies the frequency near the origin vs far away.

**Amplitude**: The difference between the brightest and the average value of the chart.

**Square Wave**: If checked, returns values that are either `0.5 + amplitude` or `0.5 - amplitude` rather than smoothly going from peak to troth.

**Mode**: Choose radial or linear.

---

### Gamma Curve DCTL
Applies the "gamma" Linear To Gamma function or Gamma To Linear function generated by [this repo](https://github.com/thatcherfreeman/log2lin-finder)

#### DCTL Parameters
**Gamma, Offset, Scale, Slope, Intercept, Cut**: These are plugged into the functions:
```python
def gamma2linear(x):
    if x < cut:
        return x * slope + intercept
    else:
        return scale * powf(x, gamma) + offset

def linear2gamma(y):
    y_cut = cut * slope + intercept
    if y < y_cut:
        return (y - intercept) / slope
    else:
        return powf((y - offset) / scale, 1.0 / gamma)
```

**Linear Gain**: This applies an exposure correction to the resulting image. If you're running Gamma2Lin, then the linear image is multiplied by this value. If you're running Lin2Gamma, then the linear image is divided by this value.

**Direction**: This allows you to specify whether to convert Gamma to Linear, or Linear to Gamma.

---

### Gamut Primaries Conversion DCTL
Converts from one set of x,y chromaticity coordinates to another. Equivalent to a CST node with the input and output gamma set to Linear and without tone mapping or OOTF. It's just a 3x3 matrix under the hood. The bulk of the logic is taken from Bruce Lindbloom's incredible [website](http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html)

#### DCTL Parameters
**Source/Target Red/Green/Blue/White x/y**: Chromaticity coordinates for the source and target color spaces, if you have either **Source Primaries** or **Target Primaries** set to Custom.

**Chromatic Adaptation**: If checked, applies CAT02 chromatic adaptation if the source and target white points are not matched, so that the net matrix maps (1, 1, 1) on the input to (1, 1, 1) on the output.

**Source/Target Primaries**: Specify your source or target primaries. If set to Custom, we will use the previous value boxes as the primaries.

**Direction**: Specify whether you want to convert from Source Primaries to the Target Primaries, or the other direction. Effectively, if set to "Target to Source" we will invert the transform.

---

### Gradient Smoothness Chart DCTL
Generates a test chart with a series of linear gradients. Each gradient is a full linear interpolation between two colors. For each band drawn, the value of the start and end color is changed. The premise of this DCTL is that you would place it towards the head of your node graph and then look at the 3D Histogram towards the end of the graph. If these straight lines remain smooth, then I would assume your series of operations is going to look reasonably good on a lot of images. If the straight lines have discontinuities or sharp angles (particularly near the achromatic axis), you'll likely have breakage in certain images.

#### DCTL Parameters
**Base Hue**: Hue angle of the left edge of the gradients.

**Angle Between Patches**: Angle added to Base Hue to compute the hue of the right edge of the gradient.

**Base Value**: Constant multiplied by the Value channel on the left side, if you want to make a gradient that has nonequal values on the left and right.

**Saturation**: Saturation of left and right edges of the gradient. Computed in HSV.

**Number of Bands**: Number of gradients to draw on the screen.

**Mid Gray**: If Band Interval is set to Exponential, this represents the target value for the middle band.

**Min/Max Clamp**: If Clamp Output is checked, then colors will be replaced with white if any channel goes outside the range of [Min Clamp, Max Clamp]

**Continuous**: If checked, fills in the plane in the rgb cube between the bands.

**Clamp Output**: If checked, replaces values > 1 with pure white so that your image doesn't have any values that go outside the unit cube.

**Band Interval**: If set to Equal, then each band will be a constant code value apart from the previous band. If set to Exponential, each band will be 2x the previous band. For pipelines expecting a log or gamma encoded image, use Equal, and for pipelines expecting a linear image, use Exponential (and probably turn off output clamping).




---
### Legacy Log Curve DCTL
Applies the "legacy" Linear To Log function or Log To Linear function generated by [this repo](https://github.com/thatcherfreeman/log2lin-finder), which is based on the formation of the old-school ACESlog.

#### DCTL Parameters
**X Shift, Y Shift, Scale, Slope, Intercept, Cut**: These are plugged into the functions:
```python
def log2lin(x):
    float tmp = _pow(2, x * scale + y_shift) + x_shift
    if (tmp < cut)
        return tmp * slope + intercept
    else:
        return tmp

def lin2log(x):
    float tmp
    if (x < cut):
        tmp = (x - intercept) / slope
    else:
        tmp = x
    return (log2(tmp - x_shift) - y_shift) / scale
```

**Linear Gain**: This applies an exposure correction to the resulting image. If you're running Log2Lin, then the linear image is multiplied by this value. If you're running Lin2Log, then the linear image is divided by this value.

**Direction**: This allows you to specify whether to convert Log to Linear, or Linear to Log.




---

### Levels Converter
Converts between full and (0-1023) legal levels (64-940)

#### DCTL Parameters
**Mode**: Indicates whether to convert to Legal or to Full levels (the direction of the transform)

**Clip**: Indicates whether to clip extreme values. If Mode is set to `Full to Legal`, then Clip will clip values outside of the range 64-940. Otherwise, clip will clip values outside of the range 0-1023.



---

### Log Curve DCTL
Applies the "exp" Linear To Log function or Log To Linear function generated by [this repo](https://github.com/thatcherfreeman/log2lin-finder)

#### DCTL Parameters
**Base, Offset, Scale, Slope, Intercept, Cut**: These are plugged into the functions:
```python
def log2linear(x):
    if (x > cut):
        return scale * pow(base, x) + offset
    else:
        return slope * x + intercept

def linear2log(y):
    if (y > slope * cut + intercept):
        return log((y - offset) / scale) / log(base)
    else:
        return (y - intercept) / slope
```

**Linear Gain**: This applies an exposure correction to the resulting image. If you're running Log2Lin, then the linear image is multiplied by this value. If you're running Lin2Log, then the linear image is divided by this value.

**Direction**: This allows you to specify whether to convert Log to Linear, or Linear to Log.


---

### Luminance
Given a color gamut, compute the luminance channel associated with those primaries (IE the Y channel after converting to CIE XYZ). Expects the image to be in a Linear state.

#### DCTL Parameters
**Color Gamut**: Select a pre-configured color gamut, or choose Custom. If Custom is selected, then the _x,y_ parameters are used to specify the gamut.

**Red/Green/Blue/White x/y**: CIEXYZ _xy_ chromaticity coordinates of the four primary values.

**Show Luminance Vector**: If checked, just outputs the RGB weights of the generated luminance vector, you can take the dot product of this color and your input color to compute the luminance.



---

### Output Blanking DCTL
Draws black bars on the top/bottom or left/right sides of the frame to mask out all but a specified aspect ratio

#### DCTL Parameters
**Aspect Ratio** The aspect ratio you want to keep after pillar/letter boxing.


---
### Polarity Checker
Lets you check if your operation results in a polarity reversal.

#### How it works
Suppose a camera is pointed at two different spectra. If Spectra 1 has greater or equal energy at all wavelengths than Spectra 2, then we would expect the measured RGB values $rgb_1$ and $rgb_2$ to be subject to: $r_1 \geq r_2$, $g_1 \geq g_2$, $b_1 \geq b_2$.

This DCTL generates random gradients of increasing energy (left to right), which you'd place before some operation. Then, after the operation, put the DCTL into `Gradient Checker` mode, and it'll highlight any pixels for which greater input energy has somehow resulted in reduced output energy.


#### DCTL Parameters
**Seed**: Random seed used to generate the gradients when set to `Gradient Generator` mode.

**Num Bands**: Number of bands shown in the frame.

**Mode**: Choose from Gradient Generator and Gradient Checker.



---
### Printer Lights
Photometric printer lights function. This DCTL expects a scene linear image and outputs a scene linear image. Applied gain for one or more channels is computed by $10^{\gamma \cdot 0.025(x - 25)}$, where $x$ is the aggregate printer light ($\text{exposure} + \text{rgbchannel} + \text{cmychannel}$) and $\gamma$ is the neg gamma.

#### DCTL Parameters
**Exposure Trim**: This adjusts the printer light setting for all channels.

**Red/Green/Blue Trim**: Adjusts the printer light setting for the corresponding single channel. Note that only this slider exists in a real film printer.

**Cyan/Magenta/Yellow Trim**: Adjusts the printer light setting for the corresponding two channels. IE increasing Cyan trim results in increasing Green and Blue trims.

**Neg Gamma**: Indicate the gamma of the negative film stock that's being printed. This is the term $\gamma$ that's multiplied in in the above expression. The print stock gamma (Slope of 3 or 4 in Log Exposure vs Density chart) will presumably be embodied downstream of this DCTL via some sort of contrast adjustment.


---

### Pure Log Curve DCTL
Applies the "pure_exp" Linear To Log function or Log To Linear function generated by [this repo](https://github.com/thatcherfreeman/log2lin-finder)

#### DCTL Parameters
**Base, Offset, Scale**: These are plugged into the functions:
```python
def log2linear(x):
    return scale * (pow(base, x) + offset)

def linear2log(y):
        return log((y / scale) - offset) / log(base)
```

**Linear Gain**: This applies an exposure correction to the resulting image. If you're running Log2Lin, then the linear image is multiplied by this value. If you're running Lin2Log, then the linear image is divided by this value.

**Direction**: This allows you to specify whether to convert Log to Linear, or Linear to Log.

---

### Quantize
Simulates the effect of saving the current image at a specified bit depth.

#### DCTL Parameters
**Bit Depth**: The number of bits to be used to represent the current 0->1 value.

**Clip**: Specifies whether to clip values greater than 1.0 or less than 0.0.

**Quantization Method** [ROUND, TRUNCATE, STOCHASTIC]: If set to Round, round each value to the nearest code value, if set to truncate, simply round down to the nearest below code value. If set to Stochastic, round up or round down with a probability equal to how close the value is to the nearest integer.


---

### Rebind LGGO DCTL
Allows you to rebind three of your LGGO controls to other controls.

#### How it works
Set up a sandwich of two of these DCTLs as the following three nodes.
1. Rebind LGGO DCTL, with mode set to "Inject Patches".
2. Lift/Gamma/Gain adjustments, or Gamma/Gain/Offset adjustments. **Make sure Lum Mix is set to 0**
3. Rebind LGGO DCTL, with mode set to "Rebind Controls" and "Wheels" set to the three wheels you want to rebind, in agreement with step (2). Customize the rebinds for each of these wheels in the below settings.

In node (1) when the mode is set to "Inject Patches", this DCTL generates a single black, white, and gray (50%) pixel in three of the corners of the frame. These three values are then sampled in node (3), where the DCTL figures out what you set for the three wheels specified in "Wheels". It then inverts your adjustment, clones out the three corner pixels, and applies an adjustment based on the rebinds and the extracted trackball values.

#### DCTL Parameters
**Mid Gray**: Indicate the value of mid gray used for the Mid Gray Preserving Gamma adjustment.

**Film Negative Gamma**: Indicate the assumed negative film gamma for the Printer Lights Gain adjustment. Adjusts the sensitivity of Printer Lights adjustments, and 0.5 is representative of real negative film.

**Flip Gamma Dir**: Inverts direction of wheels rebound to "Gamma"

**Flip Mid Gray Pres. Gamma Dir**: Inverts direction of wheels rebound to "Mid Gray Preserving Gamma"

**Mode**: Choose "Inject Patches" to insert three samples so that the primaries adjustments can be captured. Choose "Rebind Controls" after your primaries adjustments to rebind those controls

**Wheels**: Choose the three wheels that can be rebound. Do not use any wheels other than these three in your sandwiched primaries adjustment.

**Lift/Gamma/Gain/Offset Wheel Rebind**: Indicate what operation should be assigned to this wheel on your control surface.

#### Supported Operations

**Lift/Gamma/Gain/Offset**: Behaves the same as the wheel does in Resolve.

**Mid Gray Preserving Gamma**: Gamma adjustment combined with a gain adjustment that restores mid gray. Similar to gamma, but pivots around the user selected Mid Gray at the top of this DCTL.

**Max Normalized Gain**: Similar to Gain but makes it so that trackball adjustments cannot increase the signal in any channel, IE max(rgb) is fixed instead of just rec709 luminance.

**Min Normalized Offset**: Sets up your offset trackball so that it always applies a positive offset unless you lower the global offset wheel.

---
### Resize Checker DCTL
Helps you identify if you've rescaled a clip poorly, by lighting up the whole frame if the very border of the frame contains black pixels. Put this at the timeline level.

#### DCTL Parameters
**Opacity**: Choose the opacity of the magenta full frame resize warning.

**Aspect Ratio**: The aspect ratio within which to search

**Use Timeline Aspect**: If checked, ignores the **Aspect Ratio** argument and instead just uses the timeline aspect ratio.

**Output Mode**: Choose what to display. If Highlight Edges is selected, then we draw a line indicating the exact pixels that will be checked in Quality mode. If any of these white pixels is black, then the entire frame will be drawn pink. Highlight Blanking simply highlights all black pixels as green. Full Screen Warning is the same as Highlight Blanking, but it also highlights the entire frame as pink if any pixel on the border of the frame is black.

**Performance Mode**: "Performance" simply checks the pixels in the four corners and the midpoints of the edges, which will catch bad framing for all linear transforms (scale, aspect, panning, keystone correction). "Quality" mode instead checks every pixel along the border of the frame (indicated by Highlight Edges), which you'll need if you added pincushion lens distortion or corrected for barrel distortion. However, it has the downside that you're more likely to have a false positive if there's a spurrious black pixel.

---

### RGB Chips DCTL
Creates rows of colored chips at the specified increment of stops. Outputs a Linear image. This is useful in evaluating tone mapping and the "Notorious Six" problem where overexposed pure colors get mapped to pure RGBCMY primaries rather than preserving their hue.

#### DCTL Parameters
**Saturation**: Saturation of the chips. In Spherical, this is set so that 1.0 results in positive CMY colors.

**Number of Hues**: Number of rows with different hues. Set this to 3 if you want pure RGB chips, set to 6 if you want RGB CMY chips. Increase if you want more granularity.

**Number of Columns**: Number of columns to generate

**Mid Gray**: Indicates the Value that will be assigned to the middle chip

**Min/Max Clamp**: If Clamp Output is checked, then if any channel falls outside the range [Min Clamp, Max Clamp], it will be replaced with white.

**Clamp Output**: Check to remove values that fall outside the Min/Max Clamp range.

**Gray Ramp**: Adds a gray ramp to the top of the frame.

**Vertical**: Turns the chart 90 degrees so it's vertical instead.

**Band Interval**: Indicate whether bands should be placed equidistantly (Equal), or one-stop apart (Exponential). The latter is better suited for pipelines that expect a Linear image.

**Model**: Choose whether to use HSV or Spherical to generate the chips. The spherical model is scaled such that at 1.0 saturation, all tiles will fit within the cube, and at 1.0 value, white is (1.0, 1.0, 1.0).

**Continuous Mode**: Choose whether each chip should be discrete, or if hue, exposure, or both should be continuous.

**Row Gaps**: If set not to None, draws neutral stripes between the colors so adjacent rows don't mess up your perception.



---

### Safety Lines DCTL
DCTL that creates a white frame to indicate safety boundaries for the image.

#### DCTL Parameters
**Aspect Ratio**: Specify the Width to Height ratio for the drawn rectangle.

**Scale**: Size of the box, if the specified aspect ratio is wider than the frame, then 1.0 means that the width will be matched. If the specified aspect ratio is narrower than the frame, then 1.0 means that the height will be matched. Smaller values indicate a smaller drawn box.

**Alpha**: Opacity of the drawn lines.

**Line Thickness**: Thickness of the drawn box.

**Shade Darkness**: Indicates brightness of the region outside of the box.


---
### SNR Checker DCTL
Estimates signal to noise ratio of parts of the image. The methodology is that for each pixel, we sample the local area around that pixel and compute the sample mean and standard deviation, and the ratio of those two numbers is the signal to noise ratio. This method is not accurate near the edges in the frame, where the signal changes rapidly, so it should only be used to evaluate SNR in regions of fixed signal/energy. You should run this on a scene linear image if you want your results to be comparable to cined's specs. Also note some caveats, that if you have errors in the linearization and you have a lifted black point, then the "Signal" part of the SNR ratio will be raised and therefore the SNR will bottom out at a higher value in your shadows. It may make sense to offset the black point towards zero.

#### DCTL Parameters
**Window Size**: For window size $n$, we sample a $n \times n$ region of pixels. Larger gives a better estimate of sample standard deviation, but will run more slowly and potentially include more edges.

**Black Point**: Indicate the black point (corresponding to zero scene light) in case your camera's black point in linear is somehow nonzero.

**Input Mode**: Choose whether to just send in the input rgb image, or if you already computed SNR elsewhere, to send in an image where the SNR of each channel is the code value for each pixel. When in SNR mode, we can only output SNR or False Color.

**Output Mode**: Choose whether to monitor the sample mean, sample standard deviation, sample variance, sample SNR, or a false color readout. Check the code to see what the colors in the false color readout map to, but red represents 16 and below, and cyan is 2 and below.

---

### Spherical DCTL
Converts between RGB and a spherical color model. Outputs a 3-channel image, $(\theta, \phi \rho)$. $\rho$ represents the magnitude of the input color (L2 norm), $\theta$ is scaled 0-1 and represents the hue, and $\phi$ represents saturation and is scaled from 0 to $\pi / 2$.

#### DCTL Parameters
**Direction**: Indicate whether to go from RGB to spherical, or from spherical to RGB.




---

### T-Log Curve
Converts between linear and my super cool, fully-logarithmic curve. Spec for this curve is 18% gray maps to 50 IRE, then 100% IRE is middle gray plus `num_stops/2`, and 0% is middle gray minus `num_stops/2`. Every stop of dynamic range has an equal number of code values given by `100% / num_stops`. Also clamps the linear input to be >= 0.0 to avoid NaNs.

#### DCTL Parameters
**Stops of Dynamic Range**: Indicates the value of `num_stops`, number of stops between 100% and 0%.

**Exposure Compensation**: Applies this many stops of gain prior to a lin2log conversion, and removes this many stops of gain after a log2lin conversion. Convenient if you want to map a tone other than 18% gray to 50IRE, but typically you should leave this at 0.

**Direction**: Indicates whether to convert linear to tlog, or from tlog to linear.





---

### Waveform Guides
Adds a border to the image and draws on the border so that the luma waveform has a luminance scale drawn on it. Put this **after** your ODT.

#### DCTL Parameters
**Minor Line Width**: Indicates how wide the narrow dashes on the left side of the waveform are.

**Line Thickness**: How wide you want the lines on the waveform to appear.

**Text Size**: Height of characters written on the left margin.

**Margin for Text**: How much horizontal space is allocated to the characters on the left margin

**Graticule Brightness**: Allows you to increase the brightness of the drawn graticule by repeating the drawn lines and characters.

**Num Stops**: Indicates how many stops of lines to show when you have ST2084 Stops or Bt1886 Stops selected as the Waveform Scale.

**BT1886 White Point**: If BT.1886 Annex 1 is selected as the Waveform scale, this controls the white point parameter, specified by $L_W$ in the official recommendation.

**BT1886 Black Point**: If BT.1886 Annex 1 is selected as the Waveform scale, this controls the black point parameter, specified by $L_B$ in the official recommendation. If set to 0, then this is just a gamma function.

**BT1886 Gamma**: Specifies the gamma curve, the recommendation says to fix this at 2.4.

**Mid Gray Nits**: Specifies the target brightness mid gray on your monitor, as a neutral point for the Stops modes.

**Rescale Mode**: Choose from None, Fill, or Aspect. As the drawn stuff in the margins changes the remaining space in the viewer, this chooses whether to just crop in on the iamge (None), to scale the image to fill the remaining space (Fill), or to scale the image while preserving its aspect ratio.

**Waveform Scale**: Choose how the horizontal guides in the waveform are calculated. If you choose the ones that end in "Stops", then the vertical units are in stops above/below mid gray, and if you choose "Nits", then the units are in nits assuming that your display is calibrated for the specified function.


---
### White Mask DCTL
Draws a white matte around the border of the frame, in case you need to spice up your standard viewing environment.

#### DCTL Parameters
**Scaling**: The original image is resized down to this scale.

**White Point**: Code value to draw for the matte.
