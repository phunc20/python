## What Use of `partial`?
Usually, `partial` is used when

- you use a function from some library/package, which has many args you need to specify for your own usecase
- you need that function and the same args many times, for the same set of args

In Aurelien Geron's `homl1e` book, there is a good example:
```python
# Stacked Autoencoder
from functools import partial

n_inputs = 28*28  # mnist
n_hidden1 = 300
n_hidden2 = 150
n_hidden3 = n_hidden1
n_outputs = n_inputs

learning_rate = 0.01
l2_reg = 0.0001

X = tf.placeholder(tf.float32, shape=[None, n_inputs])

he_init = tf.contrib.layers.variance_scaling_initializer()
l2_regularizer =tf.contrib.layers.l2_regularizer(l2_reg)
my_dense_layer = partial(
    tf.layers.dense,
    activation=tf.nn.elu,
    kernelinitializer=he_init,
    kernel_regularizer=l2_regularizer,
)

hidden1 = my_dense_layer(X, n_hidden1)
hidden2 = my_dense_layer(hidden1, n_hidden2)
hidden3 = my_dense_layer(hidden2, n_hidden3)
outputs = my_dense_layer(hidden3, n_outputs, activation=None)
```

**Rmk.** Note that even though we have specified some arg inside `partial`, later on we can still configure that
arg to a different value.


The following is an example I created artificially, wishing to help illustrate even more on the usage of `partial`.
```python
In [1]: from functools import partial

In [2]: def about(name, age=20, job="journalist", hobby=None):
   ...:     print(f"name = {name}")
   ...:     print(f"age = {age}")
   ...:     print(f"job = {job}")
   ...:     print(f"hobby = {hobby}")
   ...:

In [3]: used_alot_about = partial(about, age=75, job="retired", hobby="mountain climbing")

In [4]: used_alot_about("Tom")
name = Tom
age = 75
job = retired
hobby = mountain climbing

In [5]: used_alot_about("Bob")
name = Bob
age = 75
job = retired
hobby = mountain climbing

In [6]: used_alot_about("Smale", age=3)
name = Smale
age = 3
job = retired
hobby = mountain climbing
```
