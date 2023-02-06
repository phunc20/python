
## Nota Bene
1. `plt.imread` will return an `np.ndarray` of `dtype` equal to `np.float32`
   (in the range of $[0,1]$) if the image file is a PNG file
   (and of `dtype` equal to `np.uint8` for all the other file formats, it seems.)
1. Be it PNG, JPEG, etc., `cv2.imread` seems to always return an `np.ndarray`
   of `dtype` equal to `np.uint8` unless otherwise specified.


## Q&A
1. `plt.imsave` cannot save grayscale image into a JPEG file?
1. How to read a JPEG grayscale image using `plt.imread`?



