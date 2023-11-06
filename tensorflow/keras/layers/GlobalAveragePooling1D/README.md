Here is an example for how to use `keras.layers.GlobalAveragePooling1D`:
```python
In [1]: shape_1d = (3,4,5); limit_1d = tf.reduce_prod(shape_1d).numpy()

In [2]: tensor_1d = tf.reshape(tf.range(limit_1d), shape_1d)

In [3]: tensor_1d
Out[3]:
<tf.Tensor: shape=(3, 4, 5), dtype=int32, numpy=
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19]],

       [[20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34],
        [35, 36, 37, 38, 39]],

       [[40, 41, 42, 43, 44],
        [45, 46, 47, 48, 49],
        [50, 51, 52, 53, 54],
        [55, 56, 57, 58, 59]]], dtype=int32)>

In [4]: tf.keras.layers.GlobalAveragePooling1D(data_format="channels_first")(tensor_1d)
Out[4]:
<tf.Tensor: shape=(3, 4), dtype=int32, numpy=
array([[ 2,  7, 12, 17],
       [22, 27, 32, 37],
       [42, 47, 52, 57]], dtype=int32)>

In [5]: tf.keras.layers.GlobalAveragePooling1D(data_format="channels_last")(tensor_1d)
Out[5]:
<tf.Tensor: shape=(3, 5), dtype=int32, numpy=
array([[ 7,  8,  9, 10, 11],
       [27, 28, 29, 30, 31],
       [47, 48, 49, 50, 51]], dtype=int32)>

In [6]: tf.keras.layers.GlobalAveragePooling1D(data_format="channels_first", keepdims=True)(tensor_1d)
Out[6]:
<tf.Tensor: shape=(3, 4, 1), dtype=int32, numpy=
array([[[ 2],
        [ 7],
        [12],
        [17]],

       [[22],
        [27],
        [32],
        [37]],

       [[42],
        [47],
        [52],
        [57]]], dtype=int32)>

In [7]: tf.keras.layers.GlobalAveragePooling1D(data_format="channels_last", keepdims=True)(tensor_1d)
Out[7]:
<tf.Tensor: shape=(3, 1, 5), dtype=int32, numpy=
array([[[ 7,  8,  9, 10, 11]],

       [[27, 28, 29, 30, 31]],

       [[47, 48, 49, 50, 51]]], dtype=int32)>

In [8]: shape_2d = (2,4,5,3); limit_2d =
  Cell In[34], line 1
    shape_2d = (2,4,5,3); limit_2d =
                                     ^
SyntaxError: invalid syntax


In [9]: shape_2d = (2,4,5,3); limit_2d = tf.reduce_prod(shape_2d).numpy()

In [10]: tensor_2d = tf.reshape(tf.range(limit_2d), shape_2d)

In [11]: tf.keras.layers.GlobalAveragePooling2D(data_format="channels_first")(tensor_2d)
Out[11]:
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[  7,  22,  37,  52],
       [ 67,  82,  97, 112]], dtype=int32)>

In [12]: tf.keras.layers.GlobalAveragePooling2D(data_format="channels_last")(tensor_2d)
Out[12]:
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[28, 29, 30],
       [88, 89, 90]], dtype=int32)>

In [13]:
```
