# Introduction

This documentation provides a quick reference and showcase of the DaVinci Color Transform Language (DCTL).

The DaVinci Color Transformation Language has a C-like syntax with some additional definitions. Users can define a video effect as plain code in a text file, then run it in Resolve as a color LUT or via the DCTL OFX or Transition Plugins. There are two types:

- A DCTL *transform* applies an effect to the frames of a clip
- A DCTL *transition* applies an effect that blends from one clip to another over **time**

A DCTL program / function / effect is commonly referred to as "a DCTL". A DCTL defines a process to generate one pixel data at each given frame's coordinates, this style of program is called a "pixel shader". The DCTL code is GPU accelerated by Resolve (supported across different platforms and graphics cards).

## How to use DCTLs?

The DaVinci Color Transform Language (DCTL) is stored in file ending with *.dctl* or *.dctle* (encrypted) extension.

#### Transform DCTLs

A Transform DCTL performs a color transform or creates some effect such as increase frame's brightness (refer to Gain.dctl sample). Users can apply the Transform DCTL in 4 ways:

 1. Create a color correction node, open context menu, and apply through LUT selection
 2. Create a color correction node, add the ResolveFX DCTL plugin, and select the desired DCTL file from DCTL list.
 3. On LUT Browser, preview result and choose **Apply LUT to Current Node**
 4. Open clip thumbnail's context menu and apply through LUT selection

#### Transition DCTLs

A Transition DCTL creates a scene transition, such as a dissolve blending between 2 clips (refer to DissolveTransition.dctl sample). Transition DCTLs can only be used in the OpenFX DCTL Transition Plugin (which is located in [ *Resolve > Edit Page > OpenFX > Transition > ResolveFX Color > DCTL* ]).
The DCTL transition plugin is used in the same way as any other transition plugins (Resolve's Video Transitions, OpenFX transitions,...). After adding the plugin, users can select a DCTL file from the DCTL List and the corresponding transition effect will be applied.

#### Encrypted DCTLs

In Resolve, users can encrypt a *.dctl* file with an expiry date to distribute an effect without revealing the content. Encrypted DCTLs have an expiration date. The encrypted *.dctle* can be distributed and used normally in any of Resolve's systems until it expires.

To encrypt a DCTL: From the LUT browser, select the desired *.dctl* file, open context menu, choose **Encrypt DCTL** option. A helper dialog will appear for user to set name, expired date and output folder for the encrypted DCTL. Output of encrypted DCTL will have *.dctle* extension.

## How to write a DCTL?

Some familiarity with the programming language C/C++ is helpful below here.

#### Main entry function requirement

The DCTL file must contain a main entry function as either **transform** or **transition**.

(*NOTE*: The line defining *transform()* is called the function signature, and for DCTLs it must match the below exactly, including parameter names)

 - **transform** for Transform DCTL

```c++
__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, __TEXTURE__ p_TexR, __TEXTURE__ p_TexG, __TEXTURE__ p_TexB)
```

The *transform* function performs a color transformation at the pixel with the coordinate `(p_X, p_Y)` on an image of size `p_Width x p_Height`.

In the first signature usage, the RGB values of the input pixel are supplied through `(p_R, p_G, p_B)`.

In the second signature usage, the texture references to the RGB planes are given. These texture references allow the developers to request the RGB values of any pixel within the image. This can be done by calling `_tex2D([texID], [posX], [posY])`, which returns a float value.

In both cases, the *transform* function must return a `float3` RGB value for each pixel at the coordinates `(p_X, p_Y)` for the result image.

  - **transition** for Transition DCTL

```c++
__DEVICE__ float4 transition(int p_Width, int p_Height, int p_X, int p_Y, __TEXTURE__ p_FromTexR, __TEXTURE__ p_FromTexG, __TEXTURE__ p_FromTexB, __TEXTURE__ p_FromTexA, __TEXTURE__ p_ToTexR, __TEXTURE__ p_ToTexG, __TEXTURE__ p_ToTexB, __TEXTURE__ p_ToTexA)
```

The *transition* function performs a blending effect from one clip to another over time. The DCTL receives 1 frame from each of the two input clips, "SourceFrom" (the clip fading out) and "SourceTo" (the clip fading in), to produce the blended result. The transition's progress is defined as TRANSITION_PROGRESS inside the code, it is a read-only value ranging from 0 (transition about to start) to 1 (transition ended), so that for example a value of 0.8 means 80% of the way through.

`(p_X, p_Y)` is output result image's coordinate,

`(p_Width, p_Height)` is image size,

`(p_FromTexR, p_FromTexG, p_FromTexB)` and `(p_ToTexR, p_ToTexG, p_ToTexB)` are "SourceFrom"/"SourceTo" texture data. Developers can access any pixel in these texture using `_tex2D([texID], [posX], [posY])` function.

The *transition* function must return a `float4` RGBA value for each pixel at the coordinates `(p_X, p_Y)` for the result image.

#### Including headers

DCTL code to be used in multiple effects can be put in a header file. To include headers in DCTL use:

```c++
#include "[pathToHeader]"
```

The path and the location of the headers must be relative to the location of DCTL file.

#### External LUTs

External Look Up Tables (LUTs) can be read from file and applied in the DCTL code using following function definitions and standards:

 - LUT definition must be inside DCTL file.
 - Users may define and apply multiple LUTs in one DCTL.
 - LUT file must be in *.cube* format, it can be 1D or 3D LUT with/without shaper LUTs.
 - To define the LUT use following function, where [*lutName*] is user-defined name, [*lutPath*] is the path to LUT file which can be absolute path or
   relative path to the DCTL file location

```c++
DEFINE_LUT([lutName], [lutPath]);
```

 - To apply the LUT use the following function, where (*r, g, b*) are LUT coordinates, and [*lutName*] is user-defined name.

```c++
APPLY_LUT(r, g, b, [lutName]);
```

 - 1D LUT/Shaper LUTs will be applied with *LINEAR* interpolation method.
 - 3D LUTs will be applied with *TRILINEAR* or *TETRAHEDRAL* interpolation, as set in Resolve with [ *Project Settings > Color Management > 3D Lookup Table Interpolation* ].

#### Inline CUBE LUT

To define an inline CUBE LUT use the below syntax
```c++
DEFINE_CUBE_LUT([lutName])
{
[LUT_Content]
}
```

The [LUT_Content] is required to be wrapped inside a pair of curly bracket '{}' and needs to follow the CUBE LUT standard. Users can define multiple CUBE LUTs inside the DCTL file and they can be placed before or after the DCTL's main transform function.

To apply the inline CUBE LUT use the following function, where (*r, g, b*) are LUT coordinates, and [*lutName*] is user-defined name in the definition.

```c++
APPLY_LUT(r, g, b, [lutName]);
```

#### DCTL syntax and support keywords

Structure can be defined using **typedef struct**, as shown in the following example.
```c++
typedef struct
{
    float c00, c01, c02;
    float c10, c11, c12;
} Matrix;
```

To declare constant memory, use `__CONSTANT__`.
```c++
__CONSTANT__ float NORM[] = {1.0f / 3.0f, 1.0f / 3.0f, 1.0f / 3.0f};
```

To pass the constant memory as a function argument, use `__CONSTANTREF__` qualifier.
```c++
__DEVICE__ float DoSomething(__CONSTANTREF__ float* p_Params)
```

`__RESOLVE_VER_MAJOR__` and `__RESOLVE_VER_MINOR__` keys are defined for users to check and guard their DCTL code as shown in the following example.

e.g. In Resolve 15.0, `__RESOLVE_VER_MAJOR__ = 15` and `__RESOLVE_VER_MINOR__ = 0`.

```c++
#if ((__RESOLVE_VER_MAJOR__ == 15) && (__RESOLVE_VER_MINOR__ == 0))
    DoSomething();
#endif
```

`DEVICE_IS_CUDA, DEVICE_IS_OPENCL, DEVICE_IS_METAL` keys are defined for users to check and execute code conditionally in CUDA, OpenCL and Metal environments respectively.
```c++
#ifdef DEVICE_IS_CUDA
    DoSomethingCUDASpecific();
#endif
```

#### Transition DCTL support keywords

`TRANSITION_PROGRESS` key is defined for user to get the current transition state. It is defined as a float value within range `[0.0f, 1.0f]`

#### DCTL OpenFX UI params definition

DCTL plugin for Transform DCTL can be added on Edit Page ( *Effects Library > OpenFX > Filters > ResolveFX Color* ) and Color Page ( *OpenFX > ResolveFX Color* )
Users can access and apply their DCTL files, which are stored in DaVinci Resolve LUT directory, through "*DCTL List*" combo box.
After updating the code in DCTL file, user can press "*Reload DCTL*" button to see the reflected result right away.
Users can generate UI elements for the DCTL plugin by defining them in DCTL file. We support 5 types of UI elements: *Float Slider*, *Integer Slider*, *Value Box*, *Check Box* and *Combo Box*.
There are maximum 64 items for each type of UI elements. The UI element is linked with respective defined variable and can be used inside the transform function.

- To define UI elements use `DEFINE_UI_PARAMS()` function as below:
```
Slider:              DEFINE_UI_PARAMS([variable name], [label], [ui element type], [default value], [min value], [max value], [step])
Value Box/Check Box: DEFINE_UI_PARAMS([variable name], [label], [ui element type], [default value])
Combo Box:           DEFINE_UI_PARAMS([variable name], [label], DCTLUI_COMBO_BOX, [default value], [enum list], [enum label list])
                     Enum list and enum's label list must be defined inside the curly brackets "{}", with each item separated by "," and they both must have the same number of items.
                     Developers can use enum value inside DCTL code to get the options, while enum label will be displayed on combo box's UI.
```
- For example:
```
DEFINE_UI_PARAMS(gainR, Red Gain, DCTLUI_SLIDER_FLOAT, 1.0, 0.0, 10.0, 0.1)
DEFINE_UI_PARAMS(iters, Iteration, DCTLUI_SLIDER_INT, 1, 0, 10, 1)
DEFINE_UI_PARAMS(gain, Master Gain, DCTLUI_VALUE_BOX, 2.0)
DEFINE_UI_PARAMS(apply, Apply, DCTLUI_CHECK_BOX, 1)
DEFINE_UI_PARAMS(opt, Channel Option, DCTLUI_COMBO_BOX, 1, { RED, GREEN, BLUE }, { Channel Red, Channel Green, Channel Blue })
```

- The [*variable name*] can be used in the transform function to reflect UI element updated value.

#### Supporting math functions

##### List of floating-point math functions available
-----------------------------------------------
```c++
float _fabs(float x)                          # Returns the absolute value of x
float _powf(float x, float y)                 # Computes x raised to the power of y
float _logf(float x)                          # Computes the value of the natural logarithm of x
float _log2f(float x)                         # Computes the value of the logarithm of x to base 2
float _log10f(float x)                        # Computes the value of the logarithm of x to base 10
float _expf(float x)                          # Computes e**x, the base-e exponential of x
float _exp2f(float x)                         # Computes 2**x, the base-2 exponential of x
float _exp10f(float x)                        # Computes 10**x, the base-10 exponential of x
float _copysignf(float x, float y)            # Returns x with its sign changed to y's
float _fmaxf(float x, float y)                # Returns x or y, whichever is larger
float _fminf(float x, float y)                # Returns x or y, whichever is smaller
float _clampf(float x, float min, float max)  # Clamps x to be within the interval [min, max]
float _saturatef(float x)                     # Clamps x to be within the interval [0.0f, 1.0f]
float _sqrtf(float x)                         # Computes the non-negative square root of x
float _ceilf(float x)                         # Returns the smallest integral value greater than or equal to x
float _floorf(float x)                        # Returns the largest integral value less than or equal to x
float _truncf(float x)                        # Returns the integral value nearest to but no larger in magnitude than x
float _round(float x)                         # Returns the integral value nearest to x rounding, with half-way cases rounded away from zero
float _fmod(float x, float y)                 # Computes the floating-point remainder of x/y
float _hypotf(float x, float y)               # Computes the square root of the sum of squares of x and y
float _cosf(float x)                          # Computes the cosine of x (measured in radians)
float _sinf(float x)                          # Computes the sine of x (measured in radians)
float _cospif(float x)                        # Computes the cosine of (x * pi) (measured in radians)
float _sinpif(float x)                        # Computes the sine of (x * pi) (measured in radians)
float _tanf(float x)                          # Computes the tangent of x (measured in radians)
float _acosf(float x)                         # Computes the principle value of the arc cosine of x
float _asinf(float x)                         # Computes the principle value of the arc sine of x
float _atan2f(float y, float x)               # Computes the principal value of the arc tangent of y/x, using the signs of both arguments to
                                                # determine the quadrant of the return value
float _acoshf(float x)                        # Computes the principle value of the inverse hyperbolic cosine of x
float _asinhf(float x)                        # Computes the principle value of the inverse hyperbolic sine of x
float _atanhf(float x)                        # Computes the inverse hyperbolic tangent of x
float _coshf(float x)                         # Computes the hyperbolic cosine of x
float _sinhf(float x)                         # Computes the hyperbolic sine of x
float _tanhf(float x)                         # Computes the hyperbolic tangent of x
float _fdimf(float x, float y)                # Returns the positive difference between x and y:  x - y if x > y, +0 if x is less than or equal to y
float _fmaf(float x, float y, float z)        # Computes (x * y) + z as a single operation
float _rsqrtf(float x)                        # Computes the reciprocal of square root of x
float _fdivide(float x, float y)              # Returns x/y
float _frecip(float x)                        # Returns 1/x
int isinf(float x)                            # Returns a non-zero value if and only if x is an infinite value
int isnan(float x)                            # Returns a non-zero value if and only if x is a NaN value
int signbit(float x)                          # Returns a non-zero value if and only if sign bit of x is set
T _mix(T x, T y, float a)                     # T is used to indicate that the function can take float, float2, float3, float4, as the type for the arguments.
                                              # Returns: (x + (y - x) * a). "a" must be a value in the range [0.0f, 1.0f]. If not, the return values are undefined.
float _frexp(float x, int exp)                # Extracts mantissa and exponent from x. The mantissa m returned is a float with magnitude in the interval [1/2, 1) or 0,
                                              # and exp is updated with integer exponent value, whereas x = m * 2^exp
float _ldexp(float x, int exp)                # Returns (x * 2^exp)
```
Note that float values must have '*f*' character at the end (e.g. 1.2f).

##### List of integer math functions available
----------------------------------------
```c++
int abs(int x)                                # Returns the absolute value of x
int min(int x, int y)                         # Returns x or y, whichever is smaller
int max(int x, int y)                         # Returns x or y, whichever is larger
```

#### Sample DCTLs
 - **ConvertToGrayScale.dctl**: Sample Transform DCTL demonstrates how to use inclusion header.
 - **Gain.dctl**: Sample Transform DCTL applies gain effect using buffer memory.
 - **GainTexture.dctl**: Sample Transform DCTL applies gain effect using texture memory.
 - **GainDCTLPlugin.dctl**: Sample Transform DCTL with custom UI definitions to be used in DCTL plugin.
 - **LUTApply.dctl**: Sample Transform DCTL applies external 3D LUT.
 - **Matrix.dctl**: Sample Transform DCTL demonstrates how to define constant memory and use support function.
 - **DissolveTransition.dctl**: Sample Transition DCTL demonstrates how to write a dissolve transition.

## ACES DCTL

ACES DCTL is a type of DCTL file that allows user to define a standard color encoding (SMPTE ST 2065-1), along with Input Transforms to convert different image sources to ACES, or Output Transforms in order to view ACES images on different types of displays. There are 2 types of ACES DCTL: parametric and non-parametric ACES transforms.

### How to use ACES DCTL
Users need to place their custom ACES DCTL files in the "ACES Transforms" folder which is located in Resolve's main application support folder. All the ACES DCTLs for IDT or ODT are required to be placed into the corresponding IDT or ODT subfolder inside the "ACES Transforms" folder.
- For MacOS: "~/Library/Application Support/Blackmagic Design/DaVinci Resolve/ACES Transforms/IDT" and "~/Library/Application Support/Blackmagic Design/DaVinci Resolve/ACES Transforms/ODT"
- For Windows: "%AppData%\Blackmagic Design\\DaVinci Resolve\\Support\\ACES Transforms\\IDT" and "%AppData%\Blackmagic Design\\DaVinci Resolve\\Support\\ACES Transforms\\ODT"
- For Linux: "~/.local/share/DaVinciResolve/ACES Transforms/IDT" and "~/.local/share/DaVinciResolve/ACES Transforms/ODT"

Resolve loads all the ACES DCTLs inside the "ACES Transforms/IDT" and "ACES Transforms/ODT" folders when started. After that, users can apply ACES DCTL in 2 ways:
- From Project Settings, when users select Color Science "ACEScc" or "ACEScct" and ACES Version "ACES 1.1", ACES DCTL can be choosen from ACES Input Device Transform and ACES Output Device Transform combo box.
- From Aces Transform plugin, they can select ACES DCTLs from the Input Transform or Output Transform combo box, provided the ACES Version is ACES 1.1.

### How to write an ACES DCTL
The ACES DCTL format follows the DCTL coding standard with extra options for users to define ACES parametric and non-parametric transforms, custom EOTF functions and custom RRT/invRRT functions.
User can define ACES transform arguments using

```c++
DEFINE_ACES_PARAM([Keys], [Values])
```

#### Non-parametric ACES Transform
When users want to write a custom non-parametric ACES transform (e.g. an IDT for new vendor camera, or an ODT for custom output screen), they are required to define the argument "IS_PARAMETRIC_ACES_TRANSFORM" as 0.

Example:
```c++
DEFINE_ACES_PARAM(IS_PARAMETRIC_ACES_TRANSFORM: 0)
```
For the non-parametric ACES transform to work properly, the custom IDT needs to transform image source data into AP0 Linear colorspace, and the custom ODT needs to treat input data coming in as AP0 Linear colorspace.
Once the users define the ACES transform as non-parametric, all other parametric params definition will be ignored if added.

#### Parametric ACES Transform
When users want to write a parametric ACES transform following ACES 1.1 standard, they are required to define all of the following fields:
- Y_MIN: black luminance (cd/m^2), value must be float.
- Y_MID: mid-point luminance (cd/m^2), value must be float.
- Y_MAX: peak white luminance (cd/m^2), value must be float.
- DISPLAY_PRI: Display primaries, value must be an array of 8 floats wrapped inside a pair of curly bracket "{}".
- LIMITING_PRI: Limiting primaries, value must be an array of 8 floats wrapped inside a pair of curly bracket "{}".
- EOTF: Display device EOTF, value must be an integer value in range [0-5] corresponding to 5 ACES's defined EOTF, or a custom EOTF function name defined by user.
- INVERSE_EOTF: Input device EOTF, value must be an integer value in range [0-5] corresponding to 5 ACES's defined EOTF, or a custom inverse EOTF function name defined by user.
- SURROUND: Viewing environment, value must be an integer value of 0 or 1 to represent boolean flag.
- STRETCH_BLACK: Stretch black luminance to a PQ code value of 0, value must be an integer value of 0 or 1 to represent boolean flag.
- D60_SIM: Is user D60 adapted, value must be an integer value of 0 or 1 to represent boolean flag.
- LEGAL_RANGE: Output to legal range, value must be an integer value of 0 or 1 to represent boolean flag.

Optional define field in ACES parametric transform:
- SKIP_STANDARD_ACES_RRT: Users can choose to run or skip standard ACES RRT (in output transform) or InvRRT (in input transform), and use their own custom RRT implementation. Value must be an integer value of 0 or 1 to represent boolean flag. The standard ACES RRT will always be used when the flag is not defined.

Example:
```c++
DEFINE_ACES_PARAM(Y_MIN: 0.0001,
                  Y_MID: 7.2,
                  Y_MAX: 108.0,
                  DISPLAY_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                  LIMITING_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                  EOTF: 0  ,
                  INVERSE_EOTF: 0,
                  SURROUND: 0,
                  STRETCH_BLACK: 1,
                  D60_SIM: 0,
                  LEGAL_RANGE: 0
                  SKIP_STANDARD_ACES_RRT: 0)
```

5 ACES defined EOTFs:
```c++
- 0: ST-2084 (PQ)
- 1: BT.1886 (Rec.709/2020 settings)
- 2: sRGB (mon_curve w/ presets)
- 3: gamma 2.6
- 4: linear (no EOTF)
- 5: HLG
```

When the transform type is input transform, it will take into account the EOTF type set in "INVERSE_EOTF", and when it is output transform it will use the EOTF type set in "EOTF".

When users want to use custom EOTF functions, they are required to provide both EOTF and INVERSE_EOTF functions. They can implement them as __DEVICE__ function and set the function name to DEFINE_ACES_PARAM accordingly.
All the users' defined ACES params settings are packed as "AcesTransformUserSettingParams* p_AcesParams", with "AcesTransformUserSettingParams" is a struct defined as below
```c++
typedef struct AcesTransformUserSettingParams
{
    float yMin;           // Black luminance (cd/m^2)
    float yMid;           // Mid-point luminance (cd/m^2)
    float yMax;           // Peak white luminance (cd/m^2)
    float displayPri[8];  // Display primaries
    float limitingPri[8]; // Limiting primaries
    int eotf;             // Display device EOTF
    int surround;         // Viewing environment
    int stretchBlack;     // Stretch black luminance to a PQ code value of 0
    int d60Sim;           // Is user D60 adapted
    int legalRange;       // Output to legal range
    int skipRRT;          // Skip the standard ACES RRT transform
} AcesTransformUserSettingParams;
```

Example:
```c++
__DEVICE__ float3 fwd_custom(float3 p_InputCV, __CONSTANTREF__ AcesTransformUserSettingParams* p_AcesParams)
{
    const float3 yMin = to_float3(p_AcesParams->yMin, p_AcesParams->yMin, p_AcesParams->yMin);
    const float3 yMax = to_float3(p_AcesParams->yMax, p_AcesParams->yMax, p_AcesParams->yMax);
    const float3 outputCV = p_InputCV * (yMax - yMin) + yMin;
    return outputCV;
}

__DEVICE__ float3 bwd_custom(float3 p_InputCV, __CONSTANTREF__ AcesTransformUserSettingParams* p_AcesParams)
{
    const float3 yMin = to_float3(p_AcesParams->yMin, p_AcesParams->yMin, p_AcesParams->yMin);
    const float3 yMax = to_float3(p_AcesParams->yMax, p_AcesParams->yMax, p_AcesParams->yMax);
    const float3 outputCV = (p_InputCV - yMin) / (yMax - yMin);
    return outputCV;
}
```

To apply the ACES transform, in the DCTL's main transform function user can call the following functions corresponding to transform type as below example:

Output Transform:
```c++
__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
{
    const float3 result = AcesOutputTransform(p_R, p_G, p_B);
    return result;
}
```

Input Transform:
```c++
__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
{
    const float3 result = AcesInvOutputTransform(p_R, p_G, p_B);
    return result;
}
```

To use custom RRT functions, users should set the params SKIP_STANDARD_ACES_RRT to 1. The RRT/invRRT function can be implemented as an __DEVICE__ function and users can call them from __DEVICE__ transform() function, or users can directly write their code inside __DEVICE__  transform() function. Nevertheless, in output transform, users should call their custom RRT before calling AcesOutputTransform() function, and in input transform, users should call their custom invRRT after calling AcesInveOutputTransform() function.

Output Transform:
```c++
__DEVICE__ float3 customRRT(float p_R, float p_G, float p_B)
{
    // RRT implementation code
}

__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
{
    // Implement your custom RRT here
    const float3 rrtResult = customRRT(p_R, p_G, p_B)

    const float3 result = AcesOutputTransform(rrtResult.x, rrtResult.y, rrtResult.z);
    return result;
}
```

Input Transform:
```c++
__DEVICE__ float3 customInvRRT(float p_R, float p_G, float p_B)
{
    // InvRRT implementation code
}

__DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
{
    const float3 result = AcesInvOutputTransform(p_R, p_G, p_B);

    // Implement your custom invRRT here
    const float3 invRRTResult = customInvRRT(result.x, result.y, result.z);

    return invRRTResult;
}
```

### Sample ACES DCTLs
- **ODT_P3D65_108.dctl**: parametric Output Transform implementation following Academy standard for P3D65 108 nits.
- **ODT_CustomRRT.dctl**: parametric Output Transform implementation that bypasses the standard ACES RRT function, and uses customRRT().
- **IDT_P3D65_108.dctl**: parametric Input Transform implementation following Academy standard for P3D65 108 nits.
- **IDT_CustomEOTF.dctl**: parametric Input Transform implementation using custom EOTF function.
- **IDT_Custom_sRGB.dctl**: non-parametric Input Transform implementation to convert sRGB to ACES data with no RRT or tonemapping.
- **ODT_Custom_sRGB.dctl**: non-parametric Output Transform implementation to converts ACES to sRGB data with no RRT or tonemapping.


## CHANGELOG
### Resolve 17.0
- Support ACES DCTL.
- Introduce _ceilf() and _floorf() functions which implicitly cast the input value to floating-point value and return floating-point result. Older version DCTL that uses deprecated _ceil() and _floor() functions are required to explicitly cast the input type to floating-point.
- Support inline CUBE LUTs.
