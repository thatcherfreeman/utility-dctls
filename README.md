# Utility DCTLS
These are DCTLs that I have developed, all in a single folder for convenience.

## Aces Exposure DCTL
DCTL that allows for adjustment of exposure in ACES. Important: It's probably better to just set your timeline color space to the ACES color space you want to use, and then to use the Exposure slider in the HDR color wheels.

### How it works
Internally, this DCTL converts ACEScc or ACEScct to Linear, and then applies a gain according to the specified exposure adjustment before converting the image back into the original color space.

### DCTL Parameters
**ACES Gamma**: Pulldown menu in which you select from ACES (Linear), ACEScc, and ACEScct. This is where you specify the gamma of the image that is being fed into this DCTL.

**Exposure Adjustment**: Specifies the number of stops to increase or decrease (negative) exposure.


## Halation DCTL
DCTL that physically emulates film halation, intended for ACES Linear AP0 images.

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