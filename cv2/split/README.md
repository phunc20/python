`cv2.split` is slower than done manually through NumPy (as of 2023/02/14).
```python
In [3]: %timeit b,g,r = cv2.split(bgr)
617 µs ± 23.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [4]: cv2.split(bgr)
Out[4]: 
(array([[255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        ...,
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255]], dtype=uint8),
 array([[255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        ...,
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255]], dtype=uint8),
 array([[255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        ...,
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255],
        [255, 255, 255, ..., 255, 255, 255]], dtype=uint8))

In [5]: %timeit b,g,r = [bgr[i] for i in range(3)]
985 ns ± 13.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```
