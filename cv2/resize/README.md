## Misunderstanding
<code><b>resize()</b></code> will switch the number of rows and cols around.


```python
In [11]: A = np.empty((128,1000,3))

In [12]: B = cv2.resize(A, (128, 700))

In [13]: B.shape
Out[13]: (700, 128, 3)

In [14]: A.shape
Out[14]: (128, 1000, 3)

```


## Truth
**No**, actually I think it is designed to be like this:
- <code><b>resize(image, (height, width))</b></code>

```python
file = tf.keras.utils.get_file(
    "grace_hopper.jpg",
    "https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg")
file
image = plt.imread(file)
image.shape
plt.imshow(image);
plt.imshow(cv2.resize(image, (100, 300)));
```
