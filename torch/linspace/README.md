`torch.linspace` is similar to both

- `MATLAB`
- and `np.linspace`

in that all three admits the syntax `linspace(start, end, n_points)` s.t.

- The last entry of the resulting array equals `end`
- The first equals `start`
- There will be exactly `n_points` element(s) in the array

```ipython
In [9]: len(torch.linspace(0,1,11))
Out[9]: 11

In [10]: torch.linspace(0,1,11)
Out[10]:
tensor([0.0000, 0.1000, 0.2000, 0.3000, 0.4000, 0.5000, 0.6000, 0.7000, 0.8000,
        0.9000, 1.0000])
```
