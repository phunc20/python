# `seqeval`
`seqeval` is a Python package to do sequence labeling evaluation.

It can be installed via
```bash
pip install seqeval
```


## Basic Usage
For example,
```python
In [42]: from seqeval.metrics import classification_report

In [43]: y_true = [["O", "B-LOC", "I-LOC", "O"], ["B-PER", "I-PER", "O"]]

In [44]: y_pred = [["O", "O", "B-LOC", "O"], ["B-PER", "I-PER", "O"]]

In [45]: print(classification_report(y_true, y_pred))
              precision    recall  f1-score   support
         LOC       0.00      0.00      0.00         1
         PER       1.00      1.00      1.00         1

   micro avg       0.50      0.50      0.50         2
   macro avg       0.50      0.50      0.50         2
weighted avg       0.50      0.50      0.50         2

In [47]: y_pred[0] = ["O", "B-LOC", "B-LOC", "O"]

In [48]: print(classification_report(y_true, y_pred))
              precision    recall  f1-score   support

         LOC       0.00      0.00      0.00         1
         PER       1.00      1.00      1.00         1

   micro avg       0.33      0.50      0.40         2
   macro avg       0.50      0.50      0.50         2
weighted avg       0.50      0.50      0.50         2

In [49]: y_pred[0] = ["O", "I-LOC", "B-LOC", "O"]

In [50]: print(classification_report(y_true, y_pred))
              precision    recall  f1-score   support

         LOC       0.00      0.00      0.00         1
         PER       1.00      1.00      1.00         1

   micro avg       0.33      0.50      0.40         2
   macro avg       0.50      0.50      0.50         2
weighted avg       0.50      0.50      0.50         2

In [51]: y_pred[0] = ["O", "I-LOC", "I-LOC", "O"]

In [52]: print(classification_report(y_true, y_pred))
              precision    recall  f1-score   support

         LOC       1.00      1.00      1.00         1
         PER       1.00      1.00      1.00         1

   micro avg       1.00      1.00      1.00         2
   macro avg       1.00      1.00      1.00         2
weighted avg       1.00      1.00      1.00         2
```

We have noticed two things:

1. The begin `"B"` is tolerant enough to allow `"I"`, just like in `In [51]`.
1. We do not calculate any performance measures for `"O"`
1. The `support` column (always equal to `2` above), so far we do not know what it is.
    - Maybe it indicates the number of non-`"O"` named entity classes.


`seqeval` can also be called from HuggingFace's ecosystem by
```python
In [60]: from datasets import load_metric
    ...: metric = load_metric("seqeval")
    ...:

In [61]: y_true = [["O", "B-LOC", "I-LOC", "O"], ["B-PER", "I-PER", "O"]]
    ...: y_pred = [["O", "O", "B-LOC", "O"], ["B-PER", "I-PER", "O"]]

In [62]: metric.compute(predictions=y_pred, references=y_true)
Out[62]: 
{'LOC': {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'number': 1},
 'PER': {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'number': 1},
 'overall_precision': 0.5,
 'overall_recall': 0.5,
 'overall_f1': 0.5,
 'overall_accuracy': 0.8571428571428571}
```

As we can see, the return value of `compute()` is bascially the same as that of `classification_report()`.


## `mode="strict"` and `scheme`










