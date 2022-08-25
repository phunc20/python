The `cv2.cvtColor()` function is quite demanding on its input args' format.
In particular, one should pay attention to
- `shape`: must be of common image shape, i.e. `shape=(w,h,c)` where `c=3`
- `dtype`
    - either in the range of `{0, 1, 2, ..., 255}` with `dtype=np.uint8`
    - or in the range of $[0,1]$ with `dtype=np.float32`

```python
In [1]: import cv2

In [2]: common_rgb_colors = {
   ...:     "black": (0,0,0),
   ...:     "white": (255,255,255),
   ...:     "red": (255,0,0),
   ...:     "green": (0,128,0),
   ...:     "blue": (0,0,255),
   ...:     "orange": (255,165,0),
   ...:     "yellow": (255,255,0),
   ...:     "gray": (128,128,128),
   ...:     "brown": (165,42,42),
   ...:     "purple": (128,0,128),
   ...: }

In [3]: color_names, rgbs = [], []
   ...: for name, rgb in common_rgb_colors.items():
   ...:     color_names.append(name)
   ...:     rgbs.append(rgb)
   ...:

In [4]: cv2.cvtColor(rgbs, cv2.COLOR_RGB2HSV)
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
Input In [4], in <cell line: 1>()
----> 1 cv2.cvtColor(rgbs, cv2.COLOR_RGB2HSV)

error: OpenCV(4.6.0) :-1: error: (-5:Bad argument) in function 'cvtColor'
> Overload resolution failed:
>  - src is not a numpy array, neither a scalar
>  - Expected Ptr<cv::UMat> for argument 'src'
```

It seems that `cv2.cvtColor()` does not accept `list` as input array. Let's
try with an ndarray.

```python
In [6]: import numpy as np

In [7]: rgbs = np.array(rgbs)

In [8]: cv2.cvtColor(rgbs, cv2.COLOR_RGB2HSV)
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
Input In [8], in <cell line: 1>()
----> 1 cv2.cvtColor(rgbs, cv2.COLOR_RGB2HSV)

error: OpenCV(4.6.0) /Users/runner/work/opencv-python/opencv-python/opencv/modules/imgproc/src/color.simd_helpers.hpp:92: error: (-2:
Unspecified error) in function 'cv::impl::(anonymous namespace)::CvtHelper<cv::impl::(anonymous namespace)::Set<3, 4, -1>, cv::impl::
(anonymous namespace)::Set<3, -1, -1>, cv::impl::(anonymous namespace)::Set<0, 5, -1>, cv::impl::(anonymous namespace)::NONE>::CvtHel
per(cv::InputArray, cv::OutputArray, int) [VScn = cv::impl::(anonymous namespace)::Set<3, 4, -1>, VDcn = cv::impl::(anonymous namespa
ce)::Set<3, -1, -1>, VDepth = cv::impl::(anonymous namespace)::Set<0, 5, -1>, sizePolicy = cv::impl::(anonymous namespace)::NONE]'
> Invalid number of channels in input image:
>     'VScn::contains(scn)'
> where
>     'scn' is 1
```

Now ndarray seems to be an acceptable input arg type; nevertheless, the error tells us that its
shape is invalid. Maybe we should make it into an array of common image shape, i.e. `(w, h, c)`
with `c` equals `3`.

```python
In [10]: cv2.cvtColor(rgbs[np.newaxis, ...], cv2.COLOR_RGB2HSV)
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
Input In [10], in <cell line: 1>()
----> 1 cv2.cvtColor(rgbs[np.newaxis, ...], cv2.COLOR_RGB2HSV)

error: OpenCV(4.6.0) /Users/runner/work/opencv-python/opencv-python/opencv/modules/imgproc/src/color.simd_helpers.hpp:94: error: (-2:
Unspecified error) in function 'cv::impl::(anonymous namespace)::CvtHelper<cv::impl::(anonymous namespace)::Set<3, 4, -1>, cv::impl::
(anonymous namespace)::Set<3, -1, -1>, cv::impl::(anonymous namespace)::Set<0, 5, -1>, cv::impl::(anonymous namespace)::NONE>::CvtHel
per(cv::InputArray, cv::OutputArray, int) [VScn = cv::impl::(anonymous namespace)::Set<3, 4, -1>, VDcn = cv::impl::(anonymous namespa
ce)::Set<3, -1, -1>, VDepth = cv::impl::(anonymous namespace)::Set<0, 5, -1>, sizePolicy = cv::impl::(anonymous namespace)::NONE]'
> Unsupported depth of input image:
>     'VDepth::contains(depth)'
> where
>     'depth' is 4 (CV_32S)
```

Hmmm, it indicates sth about  **depth**...
Let's try with the `dtype=np.uint8`.

```python
In [12]: cv2.cvtColor(rgbs[np.newaxis, ...].astype(np.uint8), cv2.COLOR_RGB2HSV)
Out[12]:
array([[[  0,   0,   0],
        [  0,   0, 255],
        [  0, 255, 255],
        [ 60, 255, 128],
        [120, 255, 255],
        [ 19, 255, 255],
        [ 30, 255, 255],
        [  0,   0, 128],
        [  0, 190, 165],
        [150, 255, 128]]], dtype=uint8)
```

Let's try with other `dtype`s.
```python
In [15]: rgbs_f64 = rgbs / 255.

In [16]: rgbs_f64.dtype
Out[16]: dtype('float64')

In [19]: cv2.cvtColor(rgbs_f64[np.newaxis], cv2.COLOR_RGB2HSV)
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
Input In [19], in <cell line: 1>()
----> 1 cv2.cvtColor(rgbs_f32[np.newaxis], cv2.COLOR_RGB2HSV)

error: OpenCV(4.6.0) /Users/runner/work/opencv-python/opencv-python/opencv/modules/imgproc/src/color.simd_helpers.hpp:94: error: (-2:
Unspecified error) in function 'cv::impl::(anonymous namespace)::CvtHelper<cv::impl::(anonymous namespace)::Set<3, 4, -1>, cv::impl::
(anonymous namespace)::Set<3, -1, -1>, cv::impl::(anonymous namespace)::Set<0, 5, -1>, cv::impl::(anonymous namespace)::NONE>::CvtHel
per(cv::InputArray, cv::OutputArray, int) [VScn = cv::impl::(anonymous namespace)::Set<3, 4, -1>, VDcn = cv::impl::(anonymous namespa
ce)::Set<3, -1, -1>, VDepth = cv::impl::(anonymous namespace)::Set<0, 5, -1>, sizePolicy = cv::impl::(anonymous namespace)::NONE]'
> Unsupported depth of input image:
>     'VDepth::contains(depth)'
> where
>     'depth' is 6 (CV_64F)

In [20]: rgbs_f32 = (rgbs / 255.).astype(np.float32)

In [22]: cv2.cvtColor(rgbs_f32[np.newaxis], cv2.COLOR_RGB2HSV)
Out[22]:
array([[[  0.        ,   0.        ,   0.        ],
        [  0.        ,   0.        ,   1.        ],
        [  0.        ,   0.9999999 ,   1.        ],
        [120.        ,   0.99999976,   0.5019608 ],
        [240.        ,   0.9999999 ,   1.        ],
        [ 38.823524  ,   0.9999999 ,   1.        ],
        [ 59.999992  ,   0.9999999 ,   1.        ],
        [  0.        ,   0.        ,   0.5019608 ],
        [  0.        ,   0.74545443,   0.64705884],
        [300.        ,   0.99999976,   0.5019608 ]]], dtype=float32)
```
