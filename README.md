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
Creates a middle gray exposure chart, a linear ramp, and several gray exposure chips that are an integer number of stops above and below middle gray. This is intended to be used in a linear gamma timeline.

### DCTL Parameters
**Number of Steps**: Specifies the number of exposure chips to be displayed in the chart. One of the ones in the middle will share its value with middle gray, and each chip to the right will have a code value double of the previous chip.

**Middle Gray Value**: Specifies the desired value of middle gray, which is 18% by default. This controls the brightness of the large chip in the middle too.



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



## Safety Lines DCTL
DCTL that creates a white frame to indicate safety boundaries for the image.

### DCTL Parameters
**Aspect Ratio**: Specify the Width to Height ratio for the drawn rectangle.

**Scale**: Size of the box, if the specified aspect ratio is wider than the frame, then 1.0 means that the width will be matched. If the specified aspect ratio is narrower than the frame, then 1.0 means that the height will be matched. Smaller values indicate a smaller drawn box.

**Alpha**: Opacity of the drawn lines.

**Line Thickness**: Thickness of the drawn box.

**Shade Darkness**: Indicates brightness of the region outside of the box.


## Saturation Adjustment DCTL
DCTL that applies Gain and Gamma controls to the Saturation of an image. Can be used in HSL saturation or HSV saturation, though note that in HSL, be sure that inputs are between 0 and 1, as saturation is poorly defined for RGB values outside of this range.

### How it works
This DCTL converts the input image to HSL or HSV, then applies a Gamma and Gain adjustment to the result. Then, it converts the image back into RGB. This formulation allows for precise control over the Sat v Sat curve, while only allowing for a nondecreasing response. IE, in Resolve's standard Sat v Sat curve, you can make the mistake of having highly saturated objects in the scene become less saturated than less saturated objects, which will typically look unnatural.

### DCTL Parameters
**Saturation Type**: Specify one of [HSL, HSV]. This converts the RGB image to HSL or HSV space depending on what is specified, and uses the saturation channel from that image. HSV will typically perform better when your input image has luminances greater than 1, but HSL will sometimes make more appealing saturation adjustments.

**Gain**: The input saturation is linearly multiplied by the Gain, so this will adjust the maximum saturation allowed in the image.

**Gamma**: This mimics the Gamma control in Resolve's Primaries wheels, applying a power function to the saturation channel. This is applied before Gain.

**Show Saturation**: This checkbox allows you to view just the saturation channel, after the Gain and Gamma adjustments have been made.
