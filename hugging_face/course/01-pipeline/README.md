classifier = pipeline("zero-shot-classification")
classifier([
    "In 2022, Russia invaded Ukraine.",
    candidate_labels=["military", "politics", "entertainment", "business"],
])

generator = pipeline("text-generation")
generator(
    "工藤 新一",
    num_return_sequences=5,
    max_length=20,
)


ValueError: Couldn't instantiate the backend tokenizer from one of:
(1) a `tokenizers` library serialization file,
(2) a slow tokenizer instance to convert or
(3) an equivalent slow tokenizer class to instantiate and convert.
You need to have sentencepiece installed to convert a slow tokenizer to a fast one.



ImportError:
T5Converter requires the protobuf library but it was not found in your environment. Checkout the instructions on th
e
installation page of its repo: https://github.com/protocolbuffers/protobuf/tree/master/python#installation and foll
ow the ones
that match your environment.

```python
In [1]: from transformers import pipeline

In [2]: classifier = pipeline("sentiment-analysis")

In [6]: classifier("I've waiting for a HuggingFace course my whole life.")
Out[6]: [{'label': 'POSITIVE', 'score': 0.9344156384468079}]

In [7]: classifier([
   ...:     "It feels like I have waited for a HuggingFace course for eternity.",
   ...:     "I wish I could hate it.",
   ...: ])
   ...:
Out[7]:
[{'label': 'NEGATIVE', 'score': 0.9855812191963196},
 {'label': 'NEGATIVE', 'score': 0.9989670515060425}]

In [9]: classifier = pipeline("zero-shot-classification")
   ...: classifier(
   ...:     "In 2022, Russia invaded Ukraine.",
   ...:     candidate_labels=["military", "politics", "entertainment", "business"],
   ...: )
   ...:
No model was supplied, defaulted to facebook/bart-large-mnli (https://huggingface.co/facebook/bart-large-mnli)
Downloading: 100%|█████████████████████████████████████████████████████████████| 1.13k/1.13k [00:00<00:00, 490kB/s]
Downloading: 100%|████████████████████████████████████████████████████████████| 1.52G/1.52G [06:53<00:00, 3.95MB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████| 26.0/26.0 [00:00<00:00, 9.97kB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████| 878k/878k [00:01<00:00, 484kB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████| 446k/446k [00:01<00:00, 358kB/s]
Downloading: 100%|█████████████████████████████████████████████████████████████| 1.29M/1.29M [00:02<00:00, 652kB/s]
Out[9]: ing:  99%|████████████████████████████████████████████████████████████▍| 1.28M/1.29M [00:02<00:00, 778kB/s]
{'sequence': 'In 2022, Russia invaded Ukraine.',
 'labels': ['military', 'politics', 'entertainment', 'business'],
 'scores': [0.7207947969436646,
  0.22250868380069733,
  0.029462415724992752,
  0.027234064415097237]}

In [10]: generator = pipeline("text-generation")
    ...: generator(
    ...:     "In this course, we will teach you how to",
    ...:     num_return_sequences=2,
    ...:     max_length=15,
    ...: )
    ...:
No model was supplied, defaulted to gpt2 (https://huggingface.co/gpt2)
Downloading: 100%|█████████████████████████████████████████████████████████████████| 665/665 [00:00<00:00, 294kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████| 523M/523M [02:06<00:00, 4.32MB/s]
Downloading: 100%|█████████████████████████████████████████████████████████████| 0.99M/0.99M [00:10<00:00, 103kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████| 446k/446k [00:04<00:00, 98.0kB/s]
Downloading: 100%|█████████████████████████████████████████████████████████████| 1.29M/1.29M [00:05<00:00, 252kB/s]
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.██████▊ | 1.27M/1.29M [00:05<00:00, 384kB/s]
Out[10]:
[{'generated_text': 'In this course, we will teach you how to learn all aspects of Python'},
 {'generated_text': 'In this course, we will teach you how to be a better driver.'}]

In [11]: generator(
    ...:     "In this course, we will teach you how to",
    ...: )
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Out[11]: [{'generated_text': 'In this course, we will teach you how to create your own app that will manage and manage all the various functions of the mobile application that you have designed and tested. With this, you will have complete knowledge in the subject areas of mobile application development'}]
```

## Specifying The Model

```python
In [4]: generator = pipeline("text-generation", model="rinna/japanese-gpt2-medium")

In [5]: generator(
   ...:     "工藤 新一",
   ...:     num_return_sequences=5,
   ...:     max_length=20,
   ...: )
   ...:
Setting `pad_token_id` to `eos_token_id`:2 for open-end generation.
Out[5]:
[{'generated_text': '工藤 新一(くどう しんいち、1911年 - 2008年3月8日'},
 {'generated_text': '工藤 新一(くどう しんいち) 声 - 鈴村健一 主人公'},
 {'generated_text': '工藤 新一(くどう あらい、1962年4月26日 - )は'},
 {'generated_text': '工藤 新一(くどう しんいち) 企画・営業担当。 元『週刊少年ジャンプ'},
 {'generated_text': '工藤 新一(くどう しんいち) 演 - 長谷川博己 主人公の'}]
```

<https://huggingface.co/models>
For more pipelines, cf. <https://huggingface.co/docs/transformers/main_classes/pipelines>


## Mask Filling

```python
In [1]: from transformers import pipeline

In [2]: unmasker = pipeline("fill-mask")
   ...:
No model was supplied, defaulted to distilroberta-base (https://huggingface.co/distilroberta-base)
Downloading: 100%|█████████████████████████████████████████████████████████████████| 480/480 [00:00<00:00, 323kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████| 316M/316M [00:59<00:00, 5.56MB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████| 878k/878k [00:01<00:00, 521kB/s]
Downloading: 100%|███████████████████████████████████████████████████████████████| 446k/446k [00:01<00:00, 378kB/s]
Downloading: 100%|█████████████████████████████████████████████████████████████| 1.29M/1.29M [00:02<00:00, 625kB/s]

In [5]: unmasker("This course will teach you all about <mask> models.", top_k=5)
Out[5]:
[{'score': 0.19619803130626678,
  'token': 30412,
  'token_str': ' mathematical',
  'sequence': 'This course will teach you all about mathematical models.'},
 {'score': 0.040527231991291046,
  'token': 38163,
  'token_str': ' computational',
  'sequence': 'This course will teach you all about computational models.'},
 {'score': 0.03301785886287689,
  'token': 27930,
  'token_str': ' predictive',
  'sequence': 'This course will teach you all about predictive models.'},
 {'score': 0.031941454857587814,
  'token': 745,
  'token_str': ' building',
  'sequence': 'This course will teach you all about building models.'},
 {'score': 0.024522870779037476,
  'token': 3034,
  'token_str': ' computer',
  'sequence': 'This course will teach you all about computer models.'}]
```

What if we have two masks in the same sentence?
```python
In [10]: unmasker("This course will <mask> you all about <mask> models.", top_k=3)
Out[10]:
[[{'score': 0.8891226649284363,
   'token': 6396,
   'token_str': ' teach',
   'sequence': '<s>This course will teach you all about<mask> models.</s>'},
  {'score': 0.08693908900022507,
   'token': 1137,
   'token_str': ' tell',
   'sequence': '<s>This course will tell you all about<mask> models.</s>'},
  {'score': 0.0075994497165083885,
   'token': 311,
   'token_str': ' show',
   'sequence': '<s>This course will show you all about<mask> models.</s>'}],
 [{'score': 0.05115402117371559,
   'token': 8568,
   'token_str': ' automotive',
   'sequence': '<s>This course will<mask> you all about automotive models.</s>'},
  {'score': 0.017702210694551468,
   'token': 745,
   'token_str': ' building',
   'sequence': '<s>This course will<mask> you all about building models.</s>'},
  {'score': 0.016906119883060455,
   'token': 3034,
   'token_str': ' computer',
   'sequence': '<s>This course will<mask> you all about computer models.</s>'}]]
```

The mask token. It seems that
- for `roberta`, the mask token is `<mask>`
- for `bert`, it's `[MASK]`

But let's see what would happen if we mix and misuse them.

## Feature Extraction
