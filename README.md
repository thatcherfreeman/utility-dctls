# Utility DCTLS
These are DCTLs that I have developed, all in a single folder for convenience.


## Aces Exposure DCTL
DCTL that allows for adjustment of exposure in ACES. Important: It's probably better to just set your timeline color space to the ACES color space you want to use, and then to use the Exposure slider in the HDR color wheels.

### How it works
Internally, this DCTL converts ACEScc or ACEScct to Linear, and then applies a gain according to the specified exposure adjustment before converting the image back into the original color space.

### DCTL Parameters
**ACES Gamma**: Pulldown menu in which you select from ACES (Linear), ACEScc, and ACEScct. This is where you specify the gamma of the image that is being fed into this DCTL.

**Exposure Adjustment**: Specifies the number of stops to increase or decrease (negative) exposure.



## Color Ramp DCTL
Creates a color ramp from 0 to 100% Hue, Saturation, or Luminance. This can be used to monitor the output of your tools and overall node pipeline.

### DCTL Parameters
**Ramp Type**: Choose from Luminance, Saturation, or Hue ramp.

**Saturation Ramp Hue**: If Saturation ramp is selected, then this controls the hue of the ramp.

**Hue Ramp Saturation**: If Hue ramp is selected, then this controls the saturation of the hue ramp.



## Exposure Chart DCTL
Creates a middle gray exposure chart, an exponential ramp, a linear ramp, and several gray exposure chips that are an integer number of stops above and below middle gray. This is intended to be used in a linear gamma timeline.

### DCTL Parameters
**Number of Steps**: Specifies the number of exposure chips to be displayed in the chart. One of the ones in the middle will share its value with middle gray, and each chip to the right will have a code value double of the previous chip.

**Middle Gray Value**: Specifies the desired value of middle gray, which is 18% by default. This controls the brightness of the large chip in the middle too.



## False Color Generator
Generates a false color conversion for linear images. Draws middle gray at the specified value and sets a gray color for the values +/- half a stop from middle gray. Then, chooses random colors for each further stop. This allows you to measure contrast ratios in-camera.

### DCTL Parameters
**Middle Gray Value**: Middle gray value], 18% by default.

**Color Chip Exposure**: Raises or lowers the exposure of the drawn color chips to make them more or less visible.

**Number of Steps**: Number of steps to convert to false color. Values outside this range will just be passed through.

**Seed**: Specifies the random seed used to generate colors



## Halation DCTL
DCTL that physically emulates film halation, intended for ACES Linear AP0 images. This is intended to be used in a linear gamma timeline.

### How Halation works
Light passes through three layers of film emulsion and various color filters, ultimately with the bottom channel being Red. Light then passes through the film base and reflects off the back of the film, and this red light then re-exposes the channels in reverse order (red, then green, then blue).

### DCTL Parameters
**Focal Length** (mm): The focal length of the lens used

**Film Base Thickness** (mm): The thickness of the film (most films are between 0.12 and 0.20 mm thick). This is used in conjunction with the focal length to determine how much larger the reflected image is than the original image. Set the film thickness to zero to remove any scaling.

**Reflection exposure lost** (stops): As light passes through the film base and reflects off the anti-halation layer, it loses brightness. This parameter controls how many stops of light are lost by the time the reflection reaches the red channel again on the rebound.

**Green exposure lost** (stops): Controls how much light is lost when the reflected light passes through the red channel and then exposes the green channel. This is added to the Reflection exposure lost.

**Blue exposure lost** (stops): Controls how much light is lost when the reflected light passes through the green channel and then exposes the blue channel. This is added to the Green exposure lost and the Reflection exposure lost.

**Blur Amount** (Thousandths of image width): The light reflection is blurry by virtue of being out of focus and by being diffused by the film base and anti-halation layer. This control represents the width of the applied blur.

**Halation Gamma**: The halation color is first raised to this power before being added to the image. This allows for creative control over the effect of halation on the tonal range of the image, though it's not physically motivated.

**Show only halation**: Enabling this checkbox shows what is added (IE arithmetic addition) to the image.

**Blur Type** [NONE, BOX BLUR, TRIANGLE BLUR, FAST BLUR]: Selects the blurring method. None will not apply any blur to the reflected image, Box Blur applies a square convolution of uniform weights, Triangle blur applies a center-weighted blurring with linear falloff, and Fast Blur is essentially a box blur that samples 9 points along the center and perimeter of a square, resulting in great runtime. Box and Triangle blur will run slower with larger blur amounts.



## Invert
Inverts the values in an image.

### DCTL Parameters
**Log Mode**: When checked, computes the inverse by taking `1 - x`. When unchecked, assumes the image is scene linear and therefore computes `1 / x`.



## Levels Converter
Converts between full and (0-1023) legal levels (64-940)

### DCTL Parameters
**Mode**: Indicates whether to convert to Legal or to Full levels (the direction of the transform)

**Clip**: Indicates whether to clip extreme values. If Mode is set to `Full to Legal`, then Clip will clip values outside of the range 64-940. Otherwise, clip will clip values outside of the range 0-1023.


## Log
For each pixel and channel, takes the logarithm.

### DCTL Parameters
**Log Base**: The base of the logarithm, 10.0 by default.



## Matrix Tester
Multiplies the RGB values of the input by a 3x3 matrix with the specified entries. Supports negative values.



## Quantize
Simulates the effect of saving the current image at a specified bit depth.

### DCTL Parameters
**Bit Depth**: The number of bits to be used to represent the current 0->1 value.

**Clip**: Specifies whether to clip values greater than 1.0 or less than 0.0.

**Quantization Method** [ROUND, TRUNCATE]: If set to Round, round each value to the nearest code value, if set to truncate, simply round down to the nearest below code value.



## Random Channel Mixer
Constructs a random RGB matrix that is some distance away from the Identity matrix. Useful when trying out lots of different looks, expects image to be converted to Linear before using.

### DCTL Parameters
**Eps**: Maximum acceptable entry-delta from the identity matrix. Essentially controls the intensity of the applied effect. In some cases, a value about 0.33 will result in division by zero errors and numerical instability when rows are rescaled.

**Seed**: Indicates the random seed used to construct the matrix. Handy if you want to remember the value for later and reproduce a certain look.

**Maintain White**: If checked, scales each row of the RGB matrix to each sum to 1. This helps keep grays neutral in the final result. If unchecked, the image can take on a tint, with luminance maintained by scaling the entire matrix to sum to 3 (but individual rows can sum to values other than 1).

**Show Matrix** [OFF, FLOAT VALUE, SCALED TEN BIT VALUE]: If set to "Float Value", the entries of the matrix are displayed, allowing you to copy the values down using the RGB picker in Fusion. If set to "Scaled Ten Bit Value", the entries of the matrix are displayed, and if you have a 10-bit color picker, the difference between the code value and 500 represents the hundreths of a point that you should enter in the corresponding entry in the RGB Mixer. IE if the top middle patch has a 10-bit code value of `496`, you would enter `-0.04` for the Green channel in the Red Output section of the RGB Mixer.



## Random Contrast Curve
Constructs a contrast curve, has the option to procedurally generate one with random parameters so you can try lots of different curves in a moment.

### DCTL Parameters
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


## RGB Chips
Creates three columns of RGB chips, and optionally CMY and Luminance chips. When the RGB mixer (or any other operation) is used, the extent to which channels have been mixed will be visible in the RGB Parade. Outputs a Linear image.

### DCTL Parameters
**Number of Steps**: Number of different luminances to display for each chip. Each chip is one stop apart (in linear).

**Exposure**: Amount of gain to be applied to the image, in stops.

**Show RGB Colors**: Displays Red, Green, and Blue charts.

**Show CMY Colors**: Displays Cyan, Magenta, and Yellow charts.

**Show Luminance**: Displays an additionall luminance chart.



## Safety Lines DCTL
DCTL that creates a white frame to indicate safety boundaries for the image.

### DCTL Parameters
**Aspect Ratio**: Specify the Width to Height ratio for the drawn rectangle.

**Scale**: Size of the box, if the specified aspect ratio is wider than the frame, then 1.0 means that the width will be matched. If the specified aspect ratio is narrower than the frame, then 1.0 means that the height will be matched. Smaller values indicate a smaller drawn box.

**Alpha**: Opacity of the drawn lines.

**Line Thickness**: Thickness of the drawn box.

**Shade Darkness**: Indicates brightness of the region outside of the box.



## Saturation Adjustment DCTL
DCTL that applies Gain and Gamma controls to the Saturation of an image. Can be used in HSL saturation or HSV saturation, though note that in HSL, be sure that inputs are between 0 and 1, as saturation is poorly defined for RGB values outside of this range. This is similar to a combination of the Color Boost (which is approximately a combination of saturation gamma + gain) and Saturation (gain) controls.

### How it works
This DCTL converts the input image to HSL or HSV, then applies a Gamma and Gain adjustment to the result. Then, it converts the image back into RGB. This formulation allows for precise control over the Sat v Sat curve, while only allowing for a nondecreasing response. IE, in Resolve's standard Sat v Sat curve, you can make the mistake of having highly saturated objects in the scene become less saturated than less saturated objects, which will typically look unnatural.

### DCTL Parameters
**Saturation Type**: Specify one of [HSL, HSV]. This converts the RGB image to HSL or HSV space depending on what is specified, and uses the saturation channel from that image. HSV will typically perform better when your input image has luminances greater than 1, but HSL will sometimes make more appealing saturation adjustments.

**Gain**: The input saturation is linearly multiplied by the Gain, so this will adjust the maximum saturation allowed in the image.

**Gamma**: This mimics the Gamma control in Resolve's Primaries wheels, applying a power function to the saturation channel. This is applied before Gain.

**Show Saturation**: This checkbox allows you to view just the saturation channel, after the Gain and Gamma adjustments have been made.

**Show Curve**: When checked, this displays the corresponding curves adjustment that's being made to the saturation channel.
