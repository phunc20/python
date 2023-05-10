


- `n_components`: `(# hidden states)`
- `n_features`: `(# observations)`
- Each row of the transition matrix should sum to `1`. The same is true for the emission matrix
    - Otherwise, you'd get an error message saying that `ValueError: emissionprob_ rows must sum to 1`
