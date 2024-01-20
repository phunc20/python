- How to check whether two tensors are copy or view?
    - One way is, say, `a, b` are two tensors, by checking
      ```
      a.storage().data_ptr() == b.storage().data_ptr()
      ```
- Indexing
    - Basic indexing (slicing, etc.) returns a view
    - Advanced indexing (list as indices of a dimension, etc.) returns a copy
    
    But assignment via either basic or advanced indexing is in-place.
    (Same as in [NumPy](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html))
    
    For example,
    ```python
    In [1]: import torch
    
    In [2]: x = torch.tensor([
       ...:     [0.0, -0.3, 0.7,],
       ...:     [-0.9, 0.1, 0.0],
       ...: ])
    
    In [3]: y0 = x[0, [True, False, True]]
       ...: y1 = x[0, 0:4:2]
       ...: print(f'{y0 = }')
       ...: print(f'{y1 = }')
    y0 = tensor([0.0000, 0.7000])
    y1 = tensor([0.0000, 0.7000])
    
    In [4]: print(f'{y0.storage().data_ptr() == x.storage().data_ptr() = }')
       ...: print(f'{y1.storage().data_ptr() == x.storage().data_ptr() = }')
    y0.storage().data_ptr() == x.storage().data_ptr() = False
    y1.storage().data_ptr() == x.storage().data_ptr() = True
    
    In [5]: y0[0] = -1
       ...: print(f'{y0 = }')
       ...: print(f'{x = }')
    y0 = tensor([-1.0000,  0.7000])
    x = tensor([[ 0.0000, -0.3000,  0.7000],
            [-0.9000,  0.1000,  0.0000]])
    
    In [6]: y1[0] = -1
       ...: print(f'{y1 = }')
       ...: print(f'{x = }')
    y1 = tensor([-1.0000,  0.7000])
    x = tensor([[-1.0000, -0.3000,  0.7000],
            [-0.9000,  0.1000,  0.0000]])
    
    In [7]:
    ```


Cf.
- <https://discuss.pytorch.org/t/does-indexing-a-tensor-return-a-copy-of-it/164905/2>
- <https://pytorch.org/docs/1.13/tensor_view.html>
- <http://blog.ezyang.com/2019/05/pytorch-internals/>
