```python
class Square(torch.autograd.Function):
    @staticmethod
    def forward(ctx, i):
        result = i**2
        ctx.save_for_backward(i)
        return result

    @staticmethod
    def backward(ctx, grad_output):
        i, = ctx.saved_tensors
        return grad_output * (2*i).conj()
```

```python
In [1]: Square.__bases__
Out[1]: (torch.autograd.function.Function,)

In [2]: torch.autograd.Function is torch.autograd.function.Function
Out[2]: True

In [3]: issubclass(Square, torch.autograd.Function)
Out[3]: True

In [4]: import inspect

In [5]: inspect.isclass(Square)
Out[5]: True
```
