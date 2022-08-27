

```python
In [9]: b = np.array([0], dtype=np.uint8)

In [10]: a = np.array([255], dtype=np.uint8)

In [12]: cv2.bitwise_or(a, b)
Out[12]: array([[255]], dtype=uint8)

In [13]: a = np.array([100], dtype=np.uint8)

In [14]: cv2.bitwise_or(a, b)
Out[14]: array([[100]], dtype=uint8)

In [16]: a = np.full((3,3), 100, dtype=np.uint8)

In [17]: b = np.zeros((3,3), dtype=np.uint8)

In [18]: cv2.bitwise_or(a, b)
Out[18]:
array([[100, 100, 100],
       [100, 100, 100],
       [100, 100, 100]], dtype=uint8)

In [19]: cv2.bitwise_or(255, 0)
Out[19]:
array([[255.],
       [  0.],
       [  0.],
       [  0.]])

In [20]: cv2.bitwise_or(10, 0)
Out[20]:
array([[10.],
       [ 0.],
       [ 0.],
       [ 0.]])
```


