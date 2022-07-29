### Grayscale
The signature of `cv2.imread()` is

```python
cv2.imread(filename: str, flags: int=cv2.IMREAD_COLOR)
```

To load an image in grayscale, aside from using `cvtColor()`, one could make use
of the `flag` arg:

```python
cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
```

Below is the list of a few of such constants in `cv2`

```python
In [6]: cv2.IMREAD_GRAYSCALE
Out[6]: 0

In [7]: cv2.IMREAD_COLOR
Out[7]: 1

In [8]: cv2.IMREAD_IGNORE_ORIENTATION
Out[8]: 128

In [9]: cv2.IMREAD_ANYDEPTH
Out[9]: 2

In [10]: cv2.IMREAD_ANYCOLOR
Out[10]: 4
```













