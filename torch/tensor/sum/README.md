This method is almost identical to `np.sum()` (and probably identical to `torch.sum()` as well), so cf. `../../../numpy/sum/README.md`

```python
In [7]: torch.arange(5)
Out[7]: tensor([0, 1, 2, 3, 4])

In [8]: torch.arange(2*3*4).reshape((2,3,4))
Out[8]:
tensor([[[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11]],

        [[12, 13, 14, 15],
         [16, 17, 18, 19],
         [20, 21, 22, 23]]])

In [9]: T = torch.arange(2*3*4).reshape((2,3,4))

In [10]: T.sum(0).shape
Out[10]: torch.Size([3, 4])

In [11]: T.sum(1).shape
Out[11]: torch.Size([2, 4])

In [12]: T.sum(2).shape
Out[12]: torch.Size([2, 3])

In [13]: T.sum(0)
Out[13]:
tensor([[12, 14, 16, 18],
        [20, 22, 24, 26],
        [28, 30, 32, 34]])

In [14]: T.sum(1)
Out[14]:
tensor([[12, 15, 18, 21],
        [48, 51, 54, 57]])

In [15]: T.sum(2)
Out[15]:
tensor([[ 6, 22, 38],
        [54, 70, 86]])
```
