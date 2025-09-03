I) Introduction:
----------------
This documentation provides a quick reference and showcase of the DaVinci Color Transform Language (DCTL) - including the syntax, API and capabilities.

The DCTL syntax is C-like with additional definitions. Users can define functions using DCTL code to create a video effect, save it to file, and run it in Resolve. Such an effect serves as a "pixel shader" program - i.e. it defines a process to generate one pixel of data at a time at each given frame's coordinates. DCTL code is GPU accelerated in DaVinci Resolve across different platforms and graphics sub-systems.

In Resolve, DCTL effects can be run as a color LUT, using the DCTL OFX plugin or the Transition Plugin. DCTL effects are commonly saved as a plain text .dctl files, but if needed, developers can further save an encrypted effect as a .dctle file for distribution. See Encryption under Types of DCTLs.

For simplicity, the document uses the term "a DCTL" to refer to a logical unit (a program or function or an effect) and the more generic "DCTL" or "DCTL code" to refer to the language and syntax.

II) Types of DCTLs:
-------------------
There are two main types of DCTLs:

    - A transform DCTL applies an effect to each frame of a single clip.
    - A transition DCTL applies an effect that blends frames from two clips over time.

A Transform DCTL performs a color transform or creates an effect (e.g increasing a frame's brightness - refer to the Gain.dctl example included). Users can apply the Transform DCTL in 4 ways:

    - Create a color correction node, open context menu, and apply through LUT selection
    - Create a color correction node, add the ResolveFX DCTL plugin, and select the desired DCTL file from DCTL list.
    - On LUT Browser, preview result and choose Apply LUT to Current Node
    - Open clip thumbnail's context menu and apply through LUT selection

A Transition DCTL creates a scene transition, such as a dissolve blending between 2 clips (refer to DissolveTransition.dctl sample). Transition DCTLs can only be used in the OpenFX DCTL Transition Plugin (which is located in [ Resolve > Edit Page > OpenFX > Transition > ResolveFX Color > DCTL ]).

The DCTL transition plugin is used in the same way as any other transition plugins (Resolve's Video Transitions, OpenFX transitions,...). After adding the plugin, users can select a DCTL file from the DCTL List and the corresponding transition effect will be applied.

Encryption:
-----------
In Resolve, users can encrypt a .dctl file with an expiry date to distribute an effect without revealing the content. The encrypted .dctle can be distributed and used normally in any of Resolve's systems until it expires.

To encrypt a DCTL: From the LUT browser, select the desired .dctl file, open context menu, choose "Encrypt DCTL" option. A helper dialog will appear for user to set name, expiration date and output folder for the encrypted DCTL. The encrypted DCTL will have a .dctle extension.

III) DCTL Syntax:
-----------------
DCTL is similar to C in syntax, and uses base C types - int, float, char*, pointer etc. Some familiarity with C programming language terminology is helpful when reading this documentation.

Additional DCTL types include the following:

    __TEXTURE__ - type for a texture reference.
    float2, float3 and float4 - vector types of 2 3 and 4 float values respectively.
    The utility functions make_float2(float,float), make_float3(float,float,float) and make_float4(float,float,float,float) can be used to contruct them.

These qualifiers are used

    __DEVICE__ - qualifier to define a function.
    __CONSTANT__ - qualifier to define a constant memory.
    __CONSTANTREF__ - qualifier for a constant memory parameter passed to a function.

Structures can be defined using "typedef struct" syntax, Example:

    typedef struct
    {
        float c00, c01, c02;
        float c10, c11, c12;
    } Matrix;

Use __CONSTANT__ to qualify constant memory variables.

    __CONSTANT__ float NORM[] = {1.0f / 3.0f, 1.0f / 3.0f, 1.0f / 3.0f};

To pass the constant memory as a function argument, use __CONSTANTREF__ qualifier.

    __DEVICE__ float DoSomething(__CONSTANTREF__ float* p_Params)

The DCTL programming environment also allows read-only access to multiple global constants. These are described in context in the sections below.

1) The Main Entry Function:
---------------------------
Each DCTL file must use a single main entry function called 'transform()' or 'transition()', with the function signatures shown below.

NOTE: Use the function definition below exactly as-is - including parameter types and names.

The Transform entry function for a Transform DCTL should be one of:

    __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
    __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, __TEXTURE__ p_TexR, __TEXTURE__ p_TexG, __TEXTURE__ p_TexB)
    __DEVICE__ float4 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B, float p_A)
    __DEVICE__ float4 transform(int p_Width, int p_Height, int p_X, int p_Y, __TEXTURE__ p_TexR, __TEXTURE__ p_TexG, __TEXTURE__ p_TexB, __TEXTURE__ p_TexA)

Description:

    This function performs a pixel transformation at offset (p_X, p_Y) on a single image (0, 0, p_Width, p_Height) with the input parameters provided.

Parameters:

    - p_Width and p_Height: the image resolution.
    - p_X and p_Y: the pixel coordinates where the transform function does the color transformation.
    - The (p_R, p_G, p_B, p_A): input pixel's RGBA values.
    - The (p_TexR, p_TexG, p_TexB, p_TexA): texture references to the RGBA planes. The function can request the RGBA values for any pixel from the image by calling _tex2D([textureVariable], [posX], [posY]), which returns a float value (posX and posY being the desired input pixel coordinates).

Returns:

    Transform function returns a float3 RGB value or float4 RGBA value (in the case of transform DCTL with alpha) for each pixel at the coordinates (p_X, p_Y) of the result image.

The Transition function for a Transition DCTL uses the following signature:

    __DEVICE__ float4 transition(int p_Width, int p_Height, int p_X, int p_Y, __TEXTURE__ p_FromTexR, __TEXTURE__ p_FromTexG, __TEXTURE__ p_FromTexB, __TEXTURE__ p_FromTexA, __TEXTURE__ p_ToTexR, __TEXTURE__ p_ToTexG,   __TEXTURE__ p_ToTexB, __TEXTURE__ p_ToTexA)

Description:

    - This function performs a blend from one clip (the 'From' clip : the clip fading out) to another (the 'To' clip : the clip fading in) over time.
    - As the transition progresses, the DCTL logic selects the appropriate image from the 'From' and 'To' clips and calls this function for each blend request. The global read-only float variable 'TRANSITION_PROGRESS', ranging from 0 (transition about to start) to 1 (transition has ended), can be used from within the function to monitor the progress of the transition. See the "Other DCTL Keywords" section.

Parameters:

    - p_Width and p_Height: the output image resolution.
    - p_X and p_Y: output pixel coordinates where the blend results are stored.
    - (p_FromTexR, p_FromTexG, p_FromTexB): RGB texture references for the 'From' clip's image at TRANSITION_PROGRESS.
    - (p_ToTexR, p_ToTexG, p_ToTexB): RGB texture references for the 'From' clip's image at TRANSITION_PROGRESS.

Similar to the second transform signature, the function can access RGB values for any pixel in the "From" and "To" textures using the _tex2D([textureVariable], [posX], [posY]) function.

Returns:

    The transition function returns a float4 (RGBA) value for each pixel at the coordinates (p_X, p_Y) for the result image.

2) Including Headers:
---------------------
You can add commonly used DCTL logic to be called in multiple effects in a header file. To include a header, add the entry:

    #include "[pathToHeader]"

The path and the location of the headers are relative to the location of DCTL file.

Once included, the functions in this header file can now be referenced and used after the inclusion point.

3) Random generator:
--------------------
Pseudo-random generates float value between [0.0f, 1.0f] with uniform distribution.

    RAND(uint p_Seed)

The RandomNoise.dctl example illustrates how RAND function together with TIMELINE_FRAME_INDEX generates different noisy frames.

4) Defining and Using LUTs:
---------------------------
Look Up Tables (LUTs) can be referenced from external files, and applied using the DEFINE_LUT and APPLY_LUT functions.

    DEFINE_LUT([lutName], [lutPath]);

Parameters:

    - [lutName] is the user-defined name of the LUT
    - [lutPath] is the path to the external LUT file. Both absolute paths and paths relative to the DCTL location can be used.

    APPLY_LUT(r, g, b, [lutName]);

Parameters:

    - (r, g, b) are LUT coordinates
    - [lutName] is the user-defined LUT name - this must match a prior DEFINE_LUT or DEFINE_CUBE_LUT call (see below).

As of DaVinci Resolve 17, LUTs can be defined inline using the DEFINE_CUBE_LUT function.

    DEFINE_CUBE_LUT([lutName])
    {
        [LUT_Content]
    }

Parameters:

    - The [LUT_Content] should be wrapped with curly brackets '{}' and needs to follow the CUBE LUT standard format.
    - These LUTs can be applied in the same way as a referenced LUT - using the APPLY_LUT function.

The following rules apply:

    - LUTs must be defined in the DCTL file before use.
    - Multiple LUTs can be defined and applied in a single DCTL.
    - Multiple CUBE LUTs can be defined in a DCTL file and can be placed before or after the DCTL's Main Entry function.
    - LUT files must be in .cube format, with 1D or 3D LUTs, with/without shaper LUTs.
        - 1D LUT/Shaper LUTs will be applied with LINEAR interpolation method.
        - 3D LUTs will be applied with TRILINEAR or TETRAHEDRAL interpolation, as set in Resolve with [ Project Settings > Color Management > 3D Lookup Table Interpolation ].

5) Other DCTL keywords:
-----------------------
__RESOLVE_VER_MAJOR__ and __RESOLVE_VER_MINOR__ keys hold version values for checking and guarding version specific DCTL logic.

Example: For Resolve 17.0, __RESOLVE_VER_MAJOR__ = 17 and __RESOLVE_VER_MINOR__ = 0.

    #if ((__RESOLVE_VER_MAJOR__ >= 17) && (__RESOLVE_VER_MINOR__ >= 0))
        CallResolve17SpecificLogic();
    #else
        CallAlternativeLogic();
    #endif

DEVICE_IS_CUDA, DEVICE_IS_OPENCL, DEVICE_IS_METAL keys are defined for users to check and execute code conditionally in CUDA, OpenCL and Metal environments respectively.

Example:

    #ifdef DEVICE_IS_CUDA
        DoSomethingCUDASpecific();
    #endif

For Transition DCTLs, the TRANSITION_PROGRESS key holds the progress of the current transition state as a float value with range [0.0f, 1.0f]. During the transition, DaVinci Resolve updates the TRANSITION_PROGRESS value and calls the transition main entry function for each image. The DissolveTransition.dctl example illustrates how to use this key.

TIMELINE_FRAME_INDEX key holds the current frame's index on timeline as an integer when using DCTL through ResolveFX DCTL plugin. When using DCTL as a LUT, TIMELINE_FRAME_INDEX is 1 as default value. The RandomNoise.dctl example illustrates how to use this key.

6) Using DCTLs as Effects With Custom UI:
-----------------------------------------
Custom DCTL effects (of the Transform DCTL type) can be added as plugins from Edit Page and Color Page effects libraries. To access them, double click or drag this plugin entry:

    - Edit page > Effects Library > OpenFX > Filters > ResolveFX Color > DCTL.
    - Color page > OpenFX > ResolveFX Color > DCTL.

Once added, click the DCTL List combo box and select the desired DCTL effect to apply the effect.

To add new DCTL effects to this list, place the appropriate DCTL file in the DaVinci Resolve LUT directory.

To edit a loaded DCTL effect:

    - Navigate to the DaVinci Resolve LUT directory in a file browser.
    - Load the appropriate DCTL file in a text editor to make changes.
    - Save the file.
    - In DaVinci Resolve's inspector, press the Reset button for the DCTL combo box to see the reflected result instantly.
    - If there is DCTL build error, the dialog "DCTL Build Error" will popup with information including of build time, error DCTL name and compilation error messages.

DaVinci Resolve supports 5 types of UI elements. With the DEFINE_UI_PARAMS function, you can define custom controls for your DCTL plugins and link them to variables in the DCTL file.

    Float Slider:        DEFINE_UI_PARAMS([variable name], [label], DCTLUI_SLIDER_FLOAT, [default value], [min value], [max value], [step])
    Int Slider:          DEFINE_UI_PARAMS([variable name], [label], DCTLUI_SLIDER_INT, [default value], [min value], [max value], [step])
    Value Box:           DEFINE_UI_PARAMS([variable name], [label], DCTLUI_VALUE_BOX, [default value])
    Check Box:           DEFINE_UI_PARAMS([variable name], [label], DCTLUI_CHECK_BOX, [default value])
    Combo Box:           DEFINE_UI_PARAMS([variable name], [label], DCTLUI_COMBO_BOX, [default value], [enum list], [enum label list])
    Color Picker:        DEFINE_UI_PARAMS([variable name], [label], DCTLUI_COLOR_PICKER, [defaultValR], [defaultValG], [defaultValB])

Each DCTL plugin can have up to 64 UI controls for each type.

Parameters:

    - The [variable name] is linked with the UI element. This variable can be used inside the transform function.
    - The [label] text appears alongside the control and describes the control to the user of the DCTL.
    - The third parameter - the ui element enum - allows DaVinci Resolve to construct the appropriate UI control.
    - The [default value], [min value], [max value] and [step] are int-based (except for the Float Slider, where they are float)
    - The [enum list] - defined in curly brackets "{}" is available for use in the Main Entry function.
    - The [enum label list] - defined as string inside curly brackets "{}" is used to indicate the enum value in the UI. It must contain the same number of items as [enum list].

Examples:

    DEFINE_UI_PARAMS(gainR, Red Gain, DCTLUI_SLIDER_FLOAT, 1.0, 0.0, 10.0, 0.1)
    DEFINE_UI_PARAMS(iters, Iteration, DCTLUI_SLIDER_INT, 1, 0, 10, 1)
    DEFINE_UI_PARAMS(gain, Master Gain, DCTLUI_VALUE_BOX, 2.0)
    DEFINE_UI_PARAMS(apply, Apply, DCTLUI_CHECK_BOX, 1)
    DEFINE_UI_PARAMS(opt, Channel Option, DCTLUI_COMBO_BOX, 1, { RED, GREEN, BLUE }, { Channel Red, Channel Green, Channel Blue })
    DEFINE_UI_PARAMS(tgtColor, Target Color, DCTLUI_COLOR_PICKER, 1.0f, 1.0f, 1.0f)

Changes to custom UI parameters - via user controls, Undo actions or from DCTL logic - are reflected both in the Resolve UI and in the DCTL variable.

Users can define custom tooltip message for DCTL UI elements using the following command:

    DEFINE_UI_TOOLTIP([label], ["Tooltip message"])

Note: Tooltip message needs to be wrapped inside a double quotation marks.

Example:

    DEFINE_UI_TOOLTIP(Target Color, "Choose target color")

7) Transform DCTL with alpha:
-----------------------------
Starting from Resolve 19.1, we support Transform DCTL with alpha through ResolveFX DCTL plugin. When users want to manipulate an image with 4 channels (RGBA), they can define a transform DCTL with alpha and apply it in the plugin.

The transform with alpha entry function should be one of:

    __DEVICE__ float4 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B, float p_A)
    __DEVICE__ float4 transform(int p_Width, int p_Height, int p_X, int p_Y, __TEXTURE__ p_TexR, __TEXTURE__ p_TexG, __TEXTURE__ p_TexB, __TEXTURE__ p_TexA)

Users can define either Straight or Premultiply alpha mode with the following tags:

    DEFINE_DCTL_ALPHA_MODE_STRAIGHT
    DEFINE_DCTL_ALPHA_MODE_PREMULTIPLY

The alpha modes for both input and output images in the DCTL plugin will be set to either Straight or Premultiply based on the defined alpha tag.

In transform DCTL with alpha, the default alpha mode is Premultiply, even if the alpha mode is not explicitly specified.

8) Supporting math functions:
-----------------------------

List of floating-point math functions available
-----------------------------------------------
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
float _atan2f(float y, float x)               # Computes the principal value of the arc tangent of y/x, using the signs of both arguments to determine the quadrant of the return value
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

Note that float values must have 'f' character at the end (e.g. 1.2f).

List of integer math functions available
----------------------------------------
int abs(int x)                                # Returns the absolute value of x
int min(int x, int y)                         # Returns x or y, whichever is smaller
int max(int x, int y)                         # Returns x or y, whichever is larger

9) Sample DCTLs:
----------------
    - ColorPicker.dctl: Sample Transform DCTL demonstrates how to define custom UI color picker and set its tooltip in the DCTL plugin.
    - ConvertToGrayScale.dctl: Sample Transform DCTL demonstrates how to use inclusion header.
    - Gain.dctl: Sample Transform DCTL applies gain effect using buffer memory.
    - GainTexture.dctl: Sample Transform DCTL applies gain effect using texture memory.
    - GainDCTLPlugin.dctl: Sample Transform DCTL with custom UI definitions to be used in DCTL plugin.
    - LUTApply.dctl: Sample Transform DCTL applies external 3D LUT.
    - Matrix.dctl: Sample Transform DCTL demonstrates how to define constant memory and use support function.
    - DissolveTransition.dctl: Sample Transition DCTL demonstrates how to write a dissolve transition.
    - RandomNoise.dctl: Sample Transform DCTL demonstrates how to use TIMELINE_FRAME_INDEX and random generator.
    - AlphaCircularWindow.dctl: Sample Transform DCTL with alpha to output a circular window on the alpha channel.

IV) ACES DCTL:
--------------
ACES DCTLs allows user to define:

    - a standard color encoding (SMPTE ST 2065-1),
    - Input Transforms to convert different image sources to ACES,
    - Output Transforms in order to view ACES images on different types of displays.

and use them to define the project's color science, or in Resolve FX ACES Transform for individual clips.

There are 2 types of ACES DCTL:

    - parametric ACES transforms
    - non-parametric ACES transforms (supported since DaVinci Resolve 17).

1. Adding a Custom ACES IDT or ODT File:
----------------------------------------
Navigate to the "ACES Transforms" folder in Resolve's main application support folder.

    - MacOS: "~/Library/Application Support/Blackmagic Design/DaVinci Resolve/ACES Transforms"
    - Windows: "%AppData%\Blackmagic Design\\DaVinci Resolve\\Support\\ACES Transforms"
    - Linux: "~/.local/share/DaVinciResolve/ACES Transforms"
    - iPadOS: "On My iPad/DaVinciResolve/ACES Transforms"

Place your custom ACES DCTL files for Input Device Transforms (IDTs) in the IDT subfolder.

Place your custom ACES DCTL files for Output Device Transforms (ODTs) in the ODT subfolder.

Start Resolve.

At start up, Resolve loads all the ACES DCTLs inside the "ACES Transforms/IDT" and "ACES Transforms/ODT" folders.

2. Using a Custom ACES IDT or ODT File:
---------------------------------------
Applying ACES transforms from Project Settings:

    - Color Science: select "ACEScc" or "ACEScct"
    - ACES Version: select ACES version 1.1 or above.
    - ACES Input Device Transform: select the required ACES DCTL IDT.
    - ACES Output Device Transform: select the required ACES DCTL ODT.

Applying ACES Transform plugins to individual clips:

    - Double click or drag this plugin entry:

        - Edit page > Effects Library > OpenFX > Filters > ResolveFX Color > ACES Transform.
        - Color page > OpenFX > ResolveFX Color > ACES Transform.

    - Once added, select the required ACES DCTLs from the Input Transform or Output Transform combo box.

3. Defining an ACES DCTL:
-------------------------
The basic ACES DCTL format is as follows:

    DEFINE_ACES_PARAM([Keys]: [Values])
    __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
    {
        const float3 result = [processing expression or function];
        return result
    }

Depending on its location, an ACES DCTL is interpreted as an IDT or an ODT.  So the DEFINE_ACES_PARAM expands its parameters into either

    - float3 AcesInvOutputTransform(float p_R, float p_G, float p_B);   // if the DCTL is an IDT
    - float3 AcesOutputTransform(float p_R, float p_G, float p_B);      // if the DCTL is an ODT.

These functions can be called from the transform main entry function.

ACES DCTLs are written as transform DCTLs in one of three ways - using:

    - a non-parametric approach and hand-rolling your own transform functions.
    - a parametric ACES transform definition with standard ACES EOTFs.
    - a parametric ACES transform definition with custom EOTF functions.

Example files for all three scenarios are available in the ACES Transform folder in the DCTL Developer documentation.

Writing a Non-Parametric ACES Transform:
----------------------------------------
Example files:

    IDT_Custom_sRGB.dctl and ODT_Custom_sRGB.dctl.

To define a Non-Parametric ACES transform (e.g. an IDT for new vendor camera, or an ODT for custom output screen), use the argument "IS_PARAMETRIC_ACES_TRANSFORM: 0".

Example:

    DEFINE_ACES_PARAM(IS_PARAMETRIC_ACES_TRANSFORM: 0)

Once defined as non-parametric, all other parameter definitions in DEFINE_ACES_PARAM are ignored.

The user then defines either:

    - a custom IDT to convert the image source to the AP0 Linear colorspace, or
    - a custom ODT to convert incoming data from the AP0 linear colorspace.

And invokes it from the main transform function.

Optional fields:

    - OUTPUT_COLORSPACE_TAG: Users can tag the output colorspace for ACES DCTL ODT file so that Resolve can set the display correspondingly and tag rendered media correctly.
                             String to represent the name of tag.
                             Tag naming is defined by extracting from Academy's odt transform official ctl "[ODT/RRTODT].Academy.[TransformName].ctl"
                             https://github.com/ampas/aces-dev/tree/master/transforms/ctl/odt
                             https://github.com/ampas/aces-dev/tree/master/transforms/ctl/outputTransform
                             e.g. "ODT.Academy.Rec2020_P3D65limited_100nits_dim.ctl" - corresponding OutputColorSpaceTag name is "Rec2020_P3D65limited_100nits_dim"
                 By default, if this tag is not present the output colorspace is assumed to be Rec 709, Gamma 2.4.

Writing a Parametric ACES Transform V1:
---------------------------------------
Example Files:

    IDT_P3D65_108.dctl and ODT_P3D65_108.dctl

Use DEFINE_ACES_PARAM to define the parametric arguments.

Parametric ACES transforms V1 are supported for ACES version 1.1 to 1.3. To write a parametric ACES transform following this standard, you need to define the following fields:

    - Y_MIN: Black luminance (cd/m^2) - float.
    - Y_MID: Mid-point luminance (cd/m^2) - float.
    - Y_MAX: Peak white luminance (cd/m^2) - float.
    - DISPLAY_PRI: Display primaries - array of 8 floats inside curly brackets "{}".
    - LIMITING_PRI: Limiting primaries - array of 8 floats inside curly brackets "{}".
    - EOTF: Display device EOTF - integer in range [0-5] (see below)
    - INVERSE_EOTF: Input device EOTF - integer in range [0-5] (see below)
    - SURROUND: Viewing environment - integer (either 0 or 1) representing a boolean flag
    - STRETCH_BLACK: Stretch black luminance to a PQ code value of 0 - integer (either 0 or 1) representing a boolean flag
    - D60_SIM: Is user D60 adapted - integer (either 0 or 1) representing a boolean flag
    - LEGAL_RANGE: Output to legal range - integer (either 0 or 1) representing a boolean flag

Optional fields:

    - SKIP_STANDARD_ACES_RRT: Users can choose to run or skip standard ACES RRT (in output transform) or InvRRT (in input transform), and use their own custom RRT implementation.
                              Integer (either 0 or 1) representing a boolean flag.
                  By default, this value is treated as 0 and the standard ACES RRT (or InvRRT) is always used.

    - OUTPUT_COLORSPACE_TAG: Users can tag the output colorspace for ACES DCTL ODT file so that Resolve can set the display correspondingly and tag rendered media correctly.
                             String to represent the name of tag.
                             Tag naming is defined by extracting from Academy's odt transform official ctl "[ODT/RRTODT].Academy.[TransformName].ctl"
                             https://github.com/ampas/aces-dev/tree/master/transforms/ctl/odt
                             https://github.com/ampas/aces-dev/tree/master/transforms/ctl/outputTransform
                             e.g. "ODT.Academy.Rec2020_P3D65limited_100nits_dim.ctl" - corresponding OutputColorSpaceTag name is "Rec2020_P3D65limited_100nits_dim"
                 By default, if this tag is not present the output colorspace is assumed to be Rec 709, Gamma 2.4.

The EOTF and INVERSE EOTF fields correspond to the following Academy standard EOTF transforms:

    - 0: ST-2084 (PQ)
    - 1: BT.1886 (Rec.709/2020 settings)
    - 2: sRGB (mon_curve w/ presets)
    - 3: gamma 2.6
    - 4: linear (no EOTF)
    - 5: HLG

The EOTF parameter value is used for ODT DCTLs and the INVERSE_EOTF parameter value is used for IDT DCTLs.

Example:

    DEFINE_ACES_PARAM(Y_MIN: 0.0001,
                      Y_MID: 7.2,
                      Y_MAX: 108.0,
                      DISPLAY_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                      LIMITING_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                      EOTF: 0,
                      INVERSE_EOTF: 0,
                      SURROUND: 0,
                      STRETCH_BLACK: 1,
                      D60_SIM: 0,
                      LEGAL_RANGE: 0,
                      SKIP_STANDARD_ACES_RRT: 0)

Writing a Parametric ACES Transform with Custom Functions:
----------------------------------------------------------
Example Files:

    IDT_CustomEOTF.dctl and ODT_CustomRRT.dctl

To write custom functions for your Parametric ACES Transform,

    - Write the parametric definition as above.
    - Define two functions for EOTF and INVERSE_EOTF transforms.
    - In the parametric definition, replace the (int) parameter values for EOTF and INVERSE_EOTF with the function names.

Example:

    // Define custom EOTF and INVERSE_EOTF functions.

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

    // Include custom functions in definition
    DEFINE_ACES_PARAM(Y_MIN: 0.0001,
                  Y_MID: 7.2,
                  Y_MAX: 108.0,
                  DISPLAY_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                  LIMITING_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                  EOTF: fwd_custom,
                  INVERSE_EOTF: bwd_custom,
                  SURROUND: 0,
                  STRETCH_BLACK: 1,
                  D60_SIM: 0,
                  LEGAL_RANGE: 0)

The second parameter in the custom functions is an input struct encapsulating the same parameters that you have defined using DEFINE_ACES_PARAM.

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

The ACES DCTL format follows the DCTL coding standard with extra options for users to define ACES parametric and non-parametric transforms, custom EOTF functions and custom RRT/invRRT functions.

Writing a Parametric ACES Transform V2:
---------------------------------------
Example Files:

    IDT_P3D65_300nits_V2.dctl and ODT_P3D65_300nits_V2.dctl

Use DEFINE_ACES_V2_PARAM to define the parametric arguments.

Parametric ACES transforms V2 are supported for ACES version 2.0 by defining the following fields:

    - PEAK_LUMINANCE: Luminance of the tone scale highlight rolloff will target in cd/m^2 (nits) - float
    - LINEAR_SCALE_FACTOR: Linear scale factor - float
    - LIMITING_PRI: Limiting primaries - array of 8 floats inside curly brackets "{}".
    - ENCODING_PRI: Encoding primaries - array of 8 floats inside curly brackets "{}".
    - EOTF: Display device EOTF - integer in range [0-7] (see below)
    - IS_SCALE_WHITE: Enable to apply scaling to compress output so that the largest channel hits 1.0 - integer (either 0 or 1) representing a boolean flag

The EOTF fields correspond to the following Academy standard EOTF transforms:

    - 0: ST-2084 (PQ)
    - 1: BT.1886 (Rec.709/2020 settings)
    - 2: sRGB (mon_curve w/ presets)
    - 3: Gamma 2.6
    - 4: Linear (no EOTF)
    - 5: HLG
    - 6: BT.1886 with Gamma 2.4
    - 7: Gamma 2.2

Example:

    DEFINE_ACES_V2_PARAM(PEAK_LUMINANCE: 625.0,
                         LINEAR_SCALE_FACTOR: 0.48,
                         LIMITING_PRI: { 0.68000, 0.32000, 0.26500, 0.69000, 0.15000, 0.06000, 0.31270, 0.32900 },
                         ENCODING_PRI: { 1.000, 0.000, 0.000, 1.000, 0.000, 0.000, 0.333, 0.333 },
                         EOTF: 0,
                         IS_SCALE_WHITE: 0)

Note: - To invoke the parametric ACES Transform V2, we use the same functionalities as V1.
      - V2 parametric definition uses new template "DEFINE_ACES_V2_PARAM" comparing to "DEFINE_ACES_PARAM" in V1.
      - V2 parametric definition doesn't support Custom EOTF and skipping RRT.
      - V2 parametric definition supports 2 new EOTF options: BT.1886 with Gamma 2.4 and Gamma 2.2.
      - To write non-parametric ACES Transform, use V1 definition DEFINE_ACES_PARAM(IS_PARAMETRIC_ACES_TRANSFORM: 0).

Invoking Parametric Transforms from the Main Transform Function:
----------------------------------------------------------------
To apply the ACES transform, call the generated AcesOutputTransform or AcesInvOutputTransform in the DCTL's main transform function:

    - For Output Transforms:

        __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
        {
            const float3 result = AcesOutputTransform(p_R, p_G, p_B);
            return result;
        }

    - For Input Transforms:

        __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
        {
            const float3 result = AcesInvOutputTransform(p_R, p_G, p_B);
            return result;
        }

If you have set "SKIP_STANDARD_ACES_RRT: 1", you will need to chain in the custom RRT or Inverse RRT as an additional step. Example:

    - Output Transform:

        __DEVICE__ float3 customRRT(float p_R, float p_G, float p_B)
        {
            // RRT implementation code
        }

        __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
        {
            // Call your custom RRT here
            const float3 rrtResult = customRRT(p_R, p_G, p_B)

            // Call AcesOutputTransform with results of the RRT call.
            const float3 result = AcesOutputTransform(rrtResult.x, rrtResult.y, rrtResult.z);
            return result;
        }

    - Input Transform:

        __DEVICE__ float3 customInvRRT(float p_R, float p_G, float p_B)
        {
            // InvRRT implementation code
        }

        __DEVICE__ float3 transform(int p_Width, int p_Height, int p_X, int p_Y, float p_R, float p_G, float p_B)
        {
            // Call AcesInvOutputTransform first
            const float3 result = AcesInvOutputTransform(p_R, p_G, p_B);

            // Call your custom Inverse RRT with the results.
            const float3 invRRTResult = customInvRRT(result.x, result.y, result.z);
            return invRRTResult;
        }

4. List of supporting output colorspace tag names:
--------------------------------------------------
    "DCDM"
    "DCDM_P3D60limited"
    "DCDM_P3D65limited"
    "P3D60_48nits"
    "P3D65_48nits"
    "P3D65_D60sim_48nits"
    "P3D65_Rec709limited_48nits"
    "P3D65_108nits_7.2nits_ST2084"
    "P3D65_1000nits_15nits_ST2084"
    "P3D65_2000nits_15nits_ST2084"
    "P3D65_4000nits_15nits_ST2084"
    "P3DCI_D60sim_48nits"
    "P3DCI_D65sim_48nits"
    "Rec709_100nits_dim"
    "Rec709_D60sim_100nits_dim"
    "Rec2020_100nits_dim"
    "Rec2020_P3D65limited_100nits_dim"
    "Rec2020_Rec709limited_100nits_dim"
    "Rec2020_1000nits_15nits_HLG"
    "Rec2020_1000nits_15nits_ST2084"
    "Rec2020_2000nits_15nits_ST2084"
    "Rec2020_4000nits_15nits_ST2084"
    "sRGB_100nits_dim"
    "sRGB_D60sim_100nits_dim"

5. Example ACES DCTLs:
----------------------
    - ODT_P3D65_108.dctl: parametric Output Transform V1 implementation following Academy standard for P3D65 108 nits.
    - ODT_CustomRRT.dctl: parametric Output Transform V1 implementation that bypasses the standard ACES RRT function, and uses customRRT().
    - ODT_Custom_sRGB.dctl: non-parametric Output Transform V1 implementation to converts ACES to sRGB data with no RRT or tonemapping.
    - ODT_P3D65_300nits_V2.dctl: parametric Output Transform V2 implementation following Academy standard for DCDM (300 nit P3-D65 Limited).

    - IDT_P3D65_108.dctl: parametric Input Transform V1 implementation following Academy standard for P3D65 108 nits.
    - IDT_CustomEOTF.dctl: parametric Input Transform V1 implementation using custom EOTF function.
    - IDT_Custom_sRGB.dctl: non-parametric Input Transform V1 implementation to convert sRGB to ACES data with no RRT or tonemapping.
    - IDT_P3D65_300nits_V2.dctl: parametric Input Transform V2 implementation following Academy standard for Inverse DCDM (300 nit P3-D65 Limited).

CHANGELOG
Resolve 17.0
    - Support ACES DCTL.
    - Introduce _ceilf() and _floorf() functions which implicitly cast the input value to floating-point value and return floating-point result.
      Older version DCTL that uses deprecated _ceil() and _floor() functions are required to explicitly cast the input type to floating-point.
    - Support inline CUBE LUTs.

Resolve 18.6
    - Support output color space tag for ACES DCTL ODT files.

Resolve 19.1
    - Support random generator RAND(uint p_Seed).
    - Support the current frame's index on timeline (TIMELINE_FRAME_INDEX) in DCTL plugin.
    - Support Transform DCTL with alpha in DCTL plugin.
    - Support custom UI element Color Picker.
    - Support custom UI element tooltip when mouse over label.
    - Support incremental step control for integer and float sliders.
    - Display encrypted DCTL's expiry date on the LUT browser list.
    - Show DCTL build error dialog when using with DCTL plugin.
    - DCTL plugin's Reset Plus button resets the current selected DCTL's custom UI values.
    - DCTL combo box's Reset button rebuilds the current selected DCTL's source code and keeps the current custom UI values if possible.
    - Remove DCTL plugin's Reload button.

Resolve 20.1
    - Support Parametric ACES Transform for ACES V2.0