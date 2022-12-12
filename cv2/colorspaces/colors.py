import cv2
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")


def h_gimp2opencv(x):
    """
    In GIMP, h ranges from 0 to 360, representing a circle

    In OpenCV, h ranges from 0 to 179, of dtype uint8
        but values larger than 179 seems to clip at 179
    """
    return int((x / 360) * 179)


def sv_gimp2opencv(x):
    """
    In GIMP, s and v range from 0 to 100, representing percentage

    In OpenCV, s and v range from 0 to 255, i.e. uint8
    """
    return int((x / 100) * 255)


# TODO: add RGB if RBG is diff in GIMP and in OpenCV
def gimp2opencv(h,s,v):
    return (
        h_gimp2opencv(h),
        sv_gimp2opencv(s),
        sv_gimp2opencv(v),
    )


def unify_format(colors):
    """
    This function serves for another function `display_colors`.
    It's main purpose is to allow input args of that function to
    be of different formats.
    """
    if isinstance(colors[0], (int, float)):
        colors = (colors,)
    else:
        if len(colors) == 1:
            if not isinstance(colors[0][0], (
                int, float,
                np.uint8, np.uint16, np.uint32, np.uint64,
                np.int8, np.int16, np.int32, np.int64,
                )
            ):
                colors = colors[0]
    return colors


def display_colors(
    *colors,
    colorspace="hsv",
    show=False,
    #text=False,
):
    """
    args
        colors
            should be RGB or HSV values.
            The following formats are accepted:
                display_colors(128,255,255)
                display_colors((128,255,255))
                display_colors(((128,255,255), (0,128,45)))
                display_colors([(128,255,255), (0,128,45)])

        colorspace, str
            either "hsv" or "rgb"
    """
    #print(f"(Before) {colors = }")
    colorspace = colorspace.lower()
    assert colorspace in ("hsv", "rgb")
    colors = unify_format(colors)
    #print(f"(After) {colors = }")
    n = len(colors)
    pixels = []
    for c in colors:
        if isinstance(c, np.ndarray):
            #pixel = c.reshape((1,1,3))
            pixel = c.astype(np.uint8).reshape((1,1,3))
        else:
            pixel = np.array(c, dtype=np.uint8).reshape((1,1,3))

        if colorspace == "hsv":
            pixel = cv2.cvtColor(pixel, cv2.COLOR_HSV2RGB)

        pixels.append(pixel)
    fig, axes = plt.subplots(1, n)
    if n == 1:
        axes.matshow(pixels[0])
        axes.set_xticks([])
        axes.set_yticks([])
    else:
        for i in range(n):
            axes[i].matshow(pixels[i])
            axes[i].set_xticks([])
            axes[i].set_yticks([])

    if show:
        plt.show()

    return fig, axes


def display_gimp_colors(
    *colors,
    colorspace="hsv",
    show=False,
):
    colorspace = colorspace.lower()
    assert colorspace in ("hsv", "rgb")
    colors = unify_format(colors)
    colors = [gimp2opencv(*color) for color in colors]
    display_colors(colors, colorspace=colorspace, show=show)
