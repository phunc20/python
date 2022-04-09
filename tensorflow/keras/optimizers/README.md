## `apply_gradients()`
This is a common method of the class of `tf.keras.optimizers.Optimizer` and its subclasses,
including `tf.keras.optimizers.SGD`, `tf.keras.optimizers.Adam`, etc.

Most of the time, users of TensorFlow will use the method `minimize()` instead, which is equiv. to
1. Compute the gradients with `tf.GradientTape`
2. Apply gradients with `apply_gradients()`

**Important.** TensorFlow users seem to be used to the following practice
- Calculate gradients in the ascending direction by `grads = tape.gradient(loss, vars)`
- Gradient descent by the optimizer's method `optimizer.apply_gradients(zip(grads, vars))`

Note that we **don't** need to add minus sign to get the descending direction; instead,
`apply_gradients()` accepts the ascending gradient and minimizes the function involved.
`minimize()` and `apply_gradients()` are two methods that are related to each other.

The following is an example showing what we describe above.
```python
In [1]: import tensorflow as tf
        from tensorflow import keras

In [2]: def f(x):
   ...:     return x**2
   ...:

In [3]: x0 = tf.Variable(0.5)
   ...: with tf.GradientTape() as tape:
   ...:     y0 = f(x0)
   ...: grad0 = tape.gradient(y0, x0)
   ...: grad0

Out[3]: <tf.Tensor: shape=(), dtype=float32, numpy=1.0>

In [4]: optimizer = keras.optimizers.Adam(learning_rate=1)

In [5]: optimizer.apply_gradients([(-grad0, x0)]); x0
Out[5]: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.4999969>
```

We see that it is bad if we feed `apply_gradients()` the descending direction:
> `x0` goes from `0.5` to `1.49`, away from the `f`'s minimum `0`

If, instead, we feed `apply_gradients()` the ascending direction, we get
```python
In [6]: x1 = tf.Variable(-0.99)
   ...: with tf.GradientTape() as tape:
   ...:     y1 = f(x1)
   ...: grad1 = tape.gradient(y1, x1)
   ...: grad1

Out[6]: <tf.Tensor: shape=(), dtype=float32, numpy=-1.98>

In [7]: optimizer.apply_gradients([(grad1, x1)]); x1
Out[7]: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=-0.2458669>
```

We are moving in the correct direction.

Therefore, what `optimizer.apply_gradients([(grad0, x0)])` does is like updating
`x0 -= eta * grad0`. As a consequence, we are always expected to transform
our problems into a minimization problem (instead of a maximization one).
Otherwise, `tf` would not know what function it is dealing with, and with
a function that is not bounded below, it will keep going downwards indefinitely.
```python
In [8]: import tensorflow as tf
   ...: from tensorflow import keras
   ...:
   ...: optimizer = keras.optimizers.Adam(learning_rate=1)
   ...:
   ...: x0 = tf.Variable(1.)
   ...: n_steps = 3_000
   ...: print_interval = 500
   ...: for i in range(1, n_steps+1):
   ...:     with tf.GradientTape() as tape:
   ...:         y0 = x0
   ...:     grad0 = tape.gradient(y0, x0)
   ...:     optimizer.apply_gradients([(grad0, x0)])
   ...:     if i % print_interval == 1:
   ...:         print(f"(step {i:03d}) x0 = {x0.numpy()}")
   ...: print(f"(step {i:03d}) x0 = {x0.numpy()}")
   ...:
(step 001) x0 = 3.159046173095703e-06
(step 501) x0 = -499.99993896484375
(step 1001) x0 = -999.9999389648438
(step 1501) x0 = -1499.9998779296875
(step 2001) x0 = -1999.9998779296875
(step 2501) x0 = -2499.999755859375
(step 3000) x0 = -2998.999755859375
```
