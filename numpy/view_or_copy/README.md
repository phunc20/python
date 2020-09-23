# Similar Concept Appears in <code>julia</code>
I was running the following code along side with another jupyter notebook on my thinkpad x220.

```python
X_train, y_train = X_train_val[train_indices], y_train_val[train_indices]
X_val, y_val = X_train_val[val_indices], y_train_val[val_indices]
X_train.shape, y_train.shape, X_val.shape, y_val.shape
```
Running two jupyter notebooks at the same time revealed the time-consuming aspect of this task.
As a consequence, it raised in me the question: <b>Wouldn't it be more efficient</b> not to name
new variables <code>X\_train, y\_train</code> and only call them with the right indices?

## To answer the question whether it concerns
<b>view</b> or <b>copy</b>, here is a code snippet which might help clarify that:

```python
In [30]: A
Out[30]:
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])

In [31]: A[:1]
Out[31]: array([[1., 1., 1.]])

In [32]: A[:1] is A[:1]
Out[32]: False

In [33]: C = A

In [34]: C is A
Out[34]: True

In [35]: D = A[...]

In [36]: D is A
Out[36]: False

```







