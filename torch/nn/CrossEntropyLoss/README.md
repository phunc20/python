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
Besides, there is an interesting input arg to `nn.CrossEntropyLoss` called `weight`.<br>
Let

- $\hat{\mathbf{y}}^{(i)}$ and $c^{(i)}$ be the $i$-th training instance, predicted logits and true integer class label, respectively

- $N$ be the number of instances
- $C$ be the number of classes
- $\mathbf{w}$ be the weight input arg to `CrossEntropyLoss`

Then the _weighted cross-entropy loss_ is defined as
$$
\text{CrossEntropyLoss} := \frac{\sum_{i=1}^{N} \mathbf{w}_{c^{(i)}} \left( -\log
\frac{\exp \hat{\mathbf{y}}^{(i)}_{c^{(i)}}}{\sum_{\xi = 1}^{C} \exp \hat{\mathbf{y}}^{(i)}_{\xi}}
\right)}{\sum_{i=1}^{N} \mathbf{w}_{c^{(i)}}},
$$

where the subscript $j$ of a vector $\mathbf{t}$ indexes the $j$-th component of that vector.

In PyTorch's documentation, it is said that this `weight` input arg is useful when the class labels are unbalanced. More precisely, how would we assign `weight` when, say, we have one particular label (say, of index `0`) that is over-populated, while all the other labels are more or less equally numerous?

First, we note that when we **multiply the weight vector by a positive constant**, the weighted cross-entropy loss is **unchanged**. In other words, only the ratio of the components of $\mathbf{w}$ matters.

This leaves us with two options

1. `weight = torch.Tensor([1e-3] + [1]*(C-1))`
    - This will penalize more heavily the cases when the true class is of index greater than `0`. It will prevent the model from labeling the non-zero classes `0`.
1. `weight = torch.Tensor([1e+3] + [1]*(C-1))`
    - This will penalize more heavily the cases when the true class is of index `0`. That is to say, when the true class of an instance is `0`, but one labels it non-zero, then one'd get a big punishment.

(**Rmk.** PyTorch requires `weight` to be of type `torch.Tensor`.)

Based on the above analysis, in the given case where index `0` is overly represented, we should probably choose the first one, i.e. `weight = torch.Tensor([1e-3] + [1]*(C-1))`. It is like we weigh the minority labels heavier than the majority labels. Or, in yet another term, we weigh the classes by the inverse of their frequencies.
