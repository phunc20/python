# `inRange`
This function usually accepts as input an image array (either
gray-scale or color image, but if it's color image, then usually
in HSV colorspace because in HSV it's easier to separate colors).
Its output is a mask, i.e. an array of shape `(n_rows, n_cols)` of
`dtype=np.uint8`, where only two values exist

- `255` for those pixels whose value lies within the specified range
- `0` otherwise

Such masks could be useful for many other further image processing, e.g.
`cv2.inpaint` for watermark, seal removal.

