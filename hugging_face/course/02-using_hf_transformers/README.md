



## Cache
When we call a checkpoint by specifying its name and when that name exists in the HF-hub, `transformers` package
will download the model's configuration file and weight file for us. By default, these two downloaded files
are cached under `$HOME/.cache/huggingface/transformers/`, which one may change
if they specify the `HF_HOME` environment variable otherwise.

**(?)** The files in `HF_HOME` are all named using unrecognizable, sha-1-like filenames.
How could we know which one is which?

**(R)** One way is to print the content of the JSON files to stdout.
```bash
$ ls ~/.cache/huggingface/transformers/*.json
/home/phunc20/.cache/huggingface/transformers/dc462194780c4638f894e183eec0e214c2891e32a0276d8437e019b6cafd4961.49eeeaed2051802f574bb8508bc9b90ddd068743c7b9c17dd1afcc18c5fc82fd.json
/home/phunc20/.cache/huggingface/transformers/ff1931049683ee1e934397a712f4202c59537de2fc0266e3587404cb18822f16.1a981b4b6ba73bb1d630760e2c7baf5bc300ce297d5bd57068fbaed633cc09f1.json

$ cat ~/.cache/huggingface/transformers/ff1931049683ee1e934397a712f4202c59537de2fc0266e3587404cb18822f16.1a981b4b6ba73bb1d630760e2c7baf5bc300ce297d5bd57068fbaed633cc09f1.json
{"url": "https://huggingface.co/microsoft/layoutlm-base-uncased/resolve/main/tokenizer_config.json", "etag": "\"252f4f7fbbe3ae65d76212dec8087988c856f024\""}
$ cat ~/.cache/huggingface/transformers/dc462194780c4638f894e183eec0e214c2891e32a0276d8437e019b6cafd4961.49eeeaed2051802f574bb8508bc9b90ddd068743c7b9c17dd1afcc18c5fc82fd.json
{"url": "https://huggingface.co/cl-tohoku/bert-base-japanese-v2/resolve/main/vocab.txt", "etag": "\"9ae1a39a04b4cdbae77b4652ab1cb8fbd54cd2b9\""}
```

To systematically find the targeted checkpoint, one could write a shell script like the one below.
```bash
for json in $(ls ~/.cache/huggingface/transformers/*.json); do
  echo $(basename "$json")
  cat $json
  printf "\n\n"
done
```





```python
In [2]: from transformers import AutoModel

In [3]: model = AutoModel.from_pretrained("bert-base-cased")
Downloading: 100%|████████████████████████████████████████████████████████████| 570/570 [00:00<00:00, 350kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████| 416M/416M [01:17<00:00, 5.61MB/s]
Some weights of the model checkpoint at bert-base-cased were not used when initializing BertModel: ['cls.seq_relationship.weight', 'cls.predictions.decoder.weight', 'cls.predictions.transform.dense.weight', 'cls.seq_relationship.bias', 'cls.predictions.bias', 'cls.predictions.transform.dense.bias', 'cls.predictions.transform.LayerNorm.weight', 'cls.predictions.transform.LayerNorm.bias']
- This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).

In [4]: import torch

In [5]: sequences = ["Hello!", "Cool.", "Nice!"]
In [6]: encoded_sequences = [
   ...:     [101, 8667, 106, 102],
   ...:     [101, 13297, 119, 102],
   ...:     [101, 8835, 106, 102],
   ...: ]

In [7]: model_inputs = torch.tensor(encoded_sequences)

In [8]: model(model_inputs)
Out[8]:
```

A few words on where the `encoded_sequences` comes from:
```python
In [52]: sequences
Out[52]: ['Hello!', 'Cool.', 'Nice!']

In [53]: tokenizer(sequences)
Out[53]: {'input_ids': [[101, 8667, 106, 102], [101, 13297, 119, 102], [101, 8835, 106, 102]], 'token_type_ids': [[0, 0, 0,
 0], [0, 0, 0, 0], [0, 0, 0, 0]], 'attention_mask': [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]}

In [55]: encoded_sequences = tokenizer(sequences)["input_ids"]

In [56]: encoded_sequences
Out[56]: [[101, 8667, 106, 102], [101, 13297, 119, 102], [101, 8835, 106, 102]]
```
More on this in the upcoming section on the topic of tokenization.


## Tokenization

Continuing on the end of last section, we see that using the `Tokenizer` object directly as a function helps
transform a text into a sequence of numbers, ready for feeding into a neural network.

But how do those numbers come about? For example, we have seen that
```python
In [52]: sequences
Out[52]: ["Hello!", "Cool.", "Nice!"]

In [56]: encoded_sequences
Out[56]: [[101, 8667, 106, 102], [101, 13297, 119, 102], [101, 8835, 106, 102]]
```

**(?)** How come there are four integer IDs for each of `"Hello!", "Cool.", "Nice!"`?<br>
**(R)** It turned out that this is BERT's encoding and

- `101` $`\mapsto`$ `[CLS]`
- `8667` $\mapsto$ `Hello`, `13297` $\mapsto$ `Cool`, `8835` $\mapsto$ `Nice`
- `106` $\mapsto$ `!`, `119` $\mapsto$ `.`
- `102` $\mapsto$ `[SEP]`

To better illustrate this, let's take an example sentence and try to 

1. do it in one single step
1. do it step by step

Let's say we use the sentence `"Jim Henson was a puppeteer."` as an example.

### One single step
```python
In [60]: tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
In [61]: model_input = tokenizer("Jim Henson was a puppeteer.")

In [62]: model_input
Out[62]: {'input_ids': [101, 3104, 1124, 15703, 1108, 170, 16797, 8284, 119, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

### Step by step
The steps are
1. Tokenization
   - Tokenization, as the name suggests, **tokenizes** or **splits** a piece of text into more basic units, e.g. splitting the sentence `"Jim Henson was a puppeteer"` into words using white space as separator:
     ```python
     In [12]: tokens = "Jim Henson was a puppeteer.".split()
     
     In [13]: tokens
     Out[13]: ['Jim', 'Henson', 'was', 'a', 'puppeteer.']
     ```
     each of `"Jim", "Henson", "was"`, etc. is then called a **token**.<br><br>
     Other common tokenization schemes include character-based tokenization, subword-based tokenization.
     ```python
     # character-based
     In [63]: tokens = [c for c in "Jim Henson was a puppeteer."]
     
     In [65]: tokens
     Out[65]: ['J', 'i', 'm', ' ', 'H', 'e', 'n', 's', 'o', 'n', ' ', 'w', 'a', 's', ' ', 'a', ' ', 'p', 'u', 'p', 'p', 'e', 't', 'e', 'e', 'r', '.']
     
     # subword-based: BERT
     In [69]: tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
     
     In [70]: tokens = tokenizer.tokenize("Jim Henson was a puppeteer.")
     
     In [71]: tokens
     Out[71]: ['Jim', 'He', '##nson', 'was', 'a', 'puppet', '##eer', '.']
     ```
     There exists many other subword-based tokenization schemes, whose tokens for the above sentence differ:
     ```python
     In [84]: tokenizer = AutoTokenizer.from_pretrained("roberta-base")
     
     In [85]: tokenizer.tokenize("Jim Henson was a puppeteer.")
     Out[85]: ['Jim', 'ĠH', 'enson', 'Ġwas', 'Ġa', 'Ġpupp', 'ete', 'er', '.']
     
     In [87]: tokenizer = AutoTokenizer.from_pretrained("albert-base-v1")
     
     In [88]: tokenizer.tokenize("Jim Henson was a puppeteer.")
     Out[88]: ['▁jim', '▁henson', '▁was', '▁a', '▁puppet', 'eer', '.']
     ```
1. Encoding
   - Encoding simply refers to the act of mapping tokens to IDs
     ```python
     In [76]: ids = tokenizer.convert_tokens_to_ids(tokens)
     
     In [77]: ids
     Out[77]: [3104, 1124, 15703, 1108, 170, 16797, 8284, 119]
     ```
     Note that `ids` are two IDs less than the `model_inputs` above, which are the BOS (Beginning of Sentence) and the EOS (End of Sentence) tokens.<br>
     There exist a few related convenience methods to `convert_tokens_to_ids`:
     ```python
     In [78]: tokenizer.convert_ids_to_tokens(ids)
     Out[78]: ['Jim', 'He', '##nson', 'was', 'a', 'puppet', '##eer', '.']
     
     In [79]: tokenizer.convert_tokens_to_string(tokens)
     Out[79]: 'Jim Henson was a puppeteer.'
     
     In [81]: tokenizer.decode(ids)
     Out[81]: 'Jim Henson was a puppeteer.'
     ```
     Note that `decode` is equiv. to the composite of `convert_ids_to_tokens` and `convert_tokens_to_string`
     ```python
     In [82]: tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(ids))
     Out[82]: 'Jim Henson was a puppeteer.'
     ```
