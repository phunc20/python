
## `from tqdm import tqdm`
Basically, `tqdm` is easy to use. Just put the thing which you want to loop thru inside `tqdm()`.
For example,
```python
import time
for i in tqdm(range(10)):
    time.sleep(1)
```

One can read and learn more from <https://pypi.org/project/tqdm/>.


## Show Progress Bar when Looping thru Generators or `tf.data.Dataset`'s
If we simply put a generator inside `tqdm()`, we will soon find out that
`tqdm` no longer provides us with a progress bar, which makes it almost
meaningless to use `tqdm`.

For small generators, one can afford doing things like
```python
for rabbit in tqdm(list(rabbits_generator)):
    make_eat_carrots(rabbit)
```

But when the generator has many items, converting it into a list before looping thru it is
unrealistic. It simply takes too much time and unnecessity.

The developpers of `tqdm` do think about this scenario, and do have a solution for this.
Simply provide another argument `total=` to `tqdm()`. This `total` argument should be specified
with the **number of elements** of your generator (or generator-like object, e.g. `tf.data.Dataset`).
For instance,
```python
for batch in tqdm(dataset, total=n_batches):
    process(btach)
```


## `tqdm` in Jupyter Notebooks
If you use `from tqdm import tqdm` in jupyter notebooks, sometimes you may find the progress bar keeps being printed
one line after another, without carriage return.

One possible solution for this is to use `from tqdm.notebook import tqdm` instead.



