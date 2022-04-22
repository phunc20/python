## How to Use `nn.CrossEntropyLoss`?
There is a little bit of nitty-gritty on how to use `nn.CrossEntropyLoss`.
Usually, when we think of cross-entropy mathematically,
we think of comparing true probability distribution and
inferred/predicted probability distribution.

However, the design of `nn.CrossEntropyLoss` expects
the inference to be logits, instead of probabilities.
In other words, the model's output layer does not need
to be `Softmax`. And, instead of true probability dist.,
`nn.CrossEntropyLoss` also expects a single integer representing the
class index of that instance's ground truth.
```python
loss = nn.CrossEntropyLoss()(logits, y_label)
```

In PyTorch's documentation, it also explicitly states
that `nn.CrossEntropyLoss()(logits, y_label) = nn.NLLLoss()(LogSoftmax(logits), y_label)`

#### `weight`
Besides, there is an interesting input arg to `nn.CrossEntropyLoss` called `weight`.
Concisely, if we let

- $\hat{\mathbf{y}}^{(i)}$ and $c^{(i)}$ be the prediction logits and the true integer class label of the $i$-th instance.
- $N$ be the number of instances
- $\mathbf{w}$ be the weight input arg

$$
\text{CrossEntropyLoss} = \frac{1}{\sum_{i=1}^{N} \mathbf{w}_{c^{i}}}
$$

