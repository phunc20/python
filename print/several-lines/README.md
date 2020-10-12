One day reading <code>Atcold</code>'s code on teaching NYU dl 2020, I saw the following code to print messages in several lines.
I find them worth sharing/taking note of.

```python
size = 70641 
sampling_rate = 22050
T = size / sampling_rate

## The following two print will give the same result.

print(f"""
x[k] has {size} samples
the sampling rate is {sampling_rate * 1e-3}kHz
x(t) is {T:.1f}s long
"""
)

print(
    f'x[k] has {size} samples',
    f'the sampling rate is {sampling_rate * 1e-3}kHz',
    f'x(t) is {T:.1f}s long'
    , sep='\n')
```

```python
In [1]: size = 70641
   ...: sampling_rate = 22050
   ...: T = size / sampling_rate

In [2]: print(f"""
   ...: x[k] has {size} samples
   ...: the sampling rate is {sampling_rate * 1e-3}kHz
   ...: x(t) is {T:.1f}s long
   ...: """
   ...: )

x[k] has 70641 samples
the sampling rate is 22.05kHz
x(t) is 3.2s long

In [3]: print(
   ...:     f'x[k] has {size} samples',
   ...:     f'the sampling rate is {sampling_rate * 1e-3}kHz',
   ...:     f'x(t) is {T:.1f}s long'
   ...:     , sep='\n')
x[k] has 70641 samples
the sampling rate is 22.05kHz
x(t) is 3.2s long

In [4]:


```



