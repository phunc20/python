import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


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


def into_ndarray(color, shape=None):
    if isinstance(color, np.ndarray):
        res = color.astype(np.uint8)
    elif isinstance(color, (tuple, list)):
        res = np.array(color, dtype=np.uint8)
    if shape:
        res = res.reshape(shape)
    return res


H_MAX = 179
def hsv_inRange(
    hsv,
    *,
    low=[170,60,85],
    high=[15,255,255],
    debug=True,
):
    #if isinstance(image, (str, Path)):
    #    bgr = cv2.imread(str(image))
    #elif isinstance(image, np.ndarray):
    #    bgr = image

    #hsv = cv2.cvtColor(
    #    bgr,
    #    cv2.COLOR_BGR2HSV,
    #)
    h,s,v = low
    H,S,V = high
    if s > S or v > V:
        raise ValueError(f"""Saturation/Value lower bound greater than upper bound:
{s = }
{S = }
{v = }
{V = }""")
    if H < h:
        low1 = np.array(low, dtype=np.uint8)
        high1 = np.array([H_MAX, S, V], dtype=np.uint8)
        mask1 = cv2.inRange(hsv, low1, high1)
        low2 = np.array([0, s, v], dtype=np.uint8)
        high2 = np.array(high, dtype=np.uint8)
        mask2 = cv2.inRange(hsv, low2, high2)
        mask = cv2.bitwise_or(mask1, mask2)
    else:
        low = np.array(low, dtype=np.uint8)
        high = np.array(high, dtype=np.uint8)
        mask = cv2.inRange(hsv, low, high)

    return mask


def rgb_inRange(
    rgb,
    *,
    low=[200,0,0],
    high=[255,30,30],
):
    r,g,b = low
    R,G,B = high
    if r > R or g > G or b > B:
        raise ValueError(f"""RGB lower bound greater than upper bound:
{r = }
{R = }
{g = }
{G = }
{b = }
{B = }""")
    low = np.array(low, dtype=np.uint8)
    high = np.array(high, dtype=np.uint8)
    mask = cv2.inRange(rgb, low, high)

    return mask


def draw_inRange_color(rgb_pixel, mask, filtered):
    fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    ax1.matshow(rgb_pixel)
    #ax1.text(-0.5, 0.25, f"hsv={hsv}",
    #         #ha="left",
    #         va="top",
    #         fontsize=8,
    #)
    ax2.matshow(mask, cmap="gray", vmin=0, vmax=255)
    ax3.matshow(filtered)
    ax1.set_title("rgb")
    ax2.set_title("mask")
    ax3.set_title("filtered")
    for ax in (ax1, ax2, ax3):
        ax.set_xticks([])
        ax.set_yticks([])
    return fig


def test_inRange(
    hsv=[0, 216, 153],
    *,
    low=np.array([140, 30, 30], dtype=np.uint8),
    high=np.array([29, 255, 255], dtype=np.uint8),
):
    hsv_pixel = into_ndarray(hsv, shape=(1,1,3))
    low = into_ndarray(low)
    high = into_ndarray(high)

    rgb_pixel = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2RGB)
    mask = cv2.inRange(hsv_pixel, low, high)
    filtered = cv2.bitwise_and(rgb_pixel, rgb_pixel, mask=mask)
    fig = draw_inRange_color(rgb_pixel, mask, filtered)
    return fig


def test_hsv_inRange(
    hsv=[0, 216, 153],
    *,
    low=np.array([140, 30, 30], dtype=np.uint8),
    high=np.array([29, 255, 255], dtype=np.uint8),
):
    hsv_pixel = into_ndarray(hsv, shape=(1,1,3))

    rgb_pixel = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2RGB)
    mask = hsv_inRange(hsv_pixel, low=low, high=high)
    filtered = cv2.bitwise_and(rgb_pixel, rgb_pixel, mask=mask)
    fig = draw_inRange_color(rgb_pixel, mask, filtered)
    return fig


def splendid_display_inRange(
    *,
    low=[165,35,120],
    high=[7,255,255],
    n_hues=5,
    n_saturations=5,
    n_values=5,
    debug=False,
):
    h,s,v = low
    H,S,V = high

    if s > S or v > V:
        raise ValueError(f"Saturation/Value lower bound greater than upper bound: {s, S, v, V = }")
    if H < h:
        H += 179

    hues = np.linspace(h, H, num=n_hues).astype(np.uint8)
    saturations = np.linspace(s, S, num=n_saturations).astype(np.uint8)
    values = np.linspace(v, V, num=n_values).astype(np.uint8)

    if debug:
        print(f"{h,s,v = }")
        print(f"{H,S,V = }")
        print(f"{hues = }")
        print(f"{saturations = }")
        print(f"{values = }")

    fig, ax = plt.subplots(n_hues, figsize=(40,100))
    for i, hue in enumerate(hues):
        if hue > 179:
            hue -= 179

        array = np.empty((n_saturations, n_values, 3), dtype=np.uint8)
        for j, value in enumerate(values):
            for k, saturation in enumerate(saturations):
                array[j, k] = (hue, saturation, value)
        array = cv2.cvtColor(array, cv2.COLOR_HSV2RGB)
        ax[i].imshow(
            array,
        )
        ax[i].set_title(
            f"{hue = }"
        )
        ax[i].set_xlabel("saturation")
        ax[i].set_xticks(range(n_saturations), saturations)

        ax[i].set_ylabel("value")
        ax[i].set_yticks(range(n_values), values)
    return fig
