## `pipeline("token-classification",`
- `aggregation_strategy` will concatenate all tokens within the same entity.
  The only difference is that, to obtain the final (confidence) score for the entity,
  you have four options.
  
  E.g. if the input sentence is `"My name is Sylvain and I work at Hugging Face in Brooklyn."`
  and for the entity `"Hugging Face"` we have
  ```python
  {'entity': 'I-ORG', 'score': 0.97389334, 'index': 12, 'word': 'Hu', 'start': 33, 'end': 35},
  {'entity': 'I-ORG', 'score': 0.976115, 'index': 13, 'word': '##gging', 'start': 35, 'end': 40},
  {'entity': 'I-ORG', 'score': 0.98879766, 'index': 14, 'word': 'Face', 'start': 41, 'end': 45},
  ```
  then
    - `"simple"` computes the mean of all tokens, i.e. `np.mean([0.97389334, 0.976115, 0.98879766])`
    - `"first"` simply takes the first score as representative, i.e. `[0.97389334, 0.976115, 0.98879766][0]`
    - `"max"` takes the maximum of all tokens, i.e. `np.max([0.97389334, 0.976115, 0.98879766])`
    - `"average"` computes the average of the "words" inside the entity, i.e. `np.mean([np.mean([0.97389334, 0.976115]), 0.98879766])` or the average of `"Hugging"` and `"Face"`







