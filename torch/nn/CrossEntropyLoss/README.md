## How to Use `nn.CrossEntropyLoss`?
There is a little bit of nitty-gritty on how to use `nn.CrossEntropyLoss`.
Usually, when we think of cross-entropy mathematically,
we think of comparing true probability distribution and
inferred probability distribution.

However, the design of `nn.CrossEntropyLoss` expects
its inference to be logits, instead of probability.
In other words, the model's output layer does not need
to be `Softmax`. And, instead of true probability dist.,
PyTorch also expects a single integer representing the
class index of that instance's ground truth.
```python
loss = nn.CrossEntropyLoss()(logits, y_label)
```

In PyTorch's documentation, it also explicitly states
that `nn.CrossEntropyLoss()(logits, y_label) = nn.NLLLoss()(LogSoftmax(logits), y_label)`
