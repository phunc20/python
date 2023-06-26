## `huggingface_hub`
People seems to name their tokenizer and model with the same name, e.g.
[`roberta-base`](https://huggingface.co/roberta-base/tree/main).

Examing the files closer, it seems to suggest that it suffices to use the
method `push_to_hub` of both the tokenizer and the model to push their
separate related files onto the same remote directory. E.g.

- `tokenizer.push_to_hub("phunc20/vina-cased")`
- `model.push_to_hub("phunc20/vina-cased")`

