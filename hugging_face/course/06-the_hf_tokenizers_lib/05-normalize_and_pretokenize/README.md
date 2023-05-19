- The diff btw a fast tokenizer and a (non-fast) tokenizer
  ```python
  In [7]: from transformers import AutoTokenizer
     ...:
     ...: tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
     ...: print(type(tokenizer))
     ...: print(type(tokenizer.backend_tokenizer))
  <class 'transformers.models.bert.tokenization_bert_fast.BertTokenizerFast'>
  <class 'tokenizers.Tokenizer'>
  ```
- pre-tokenization: The most common pre-tokenization is to split text by spaces **and isolates the punctuations**, e.g.
  `"hello, how are u tday?"` becomes `["hello", ",", "how", "are", "u", "tday", "?"]`
    - Offsets to record the relationships of the pre-tokenized tokens to the original string:
      ```python
      In [9]: from transformers import AutoTokenizer
         ...:
         ...: tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
         ...: sent = "Hello, how are  you?"
         ...: tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(sent)
         ...:
      Out[9]:
      [('Hello', (0, 5)),
       (',', (5, 6)),
       ('how', (7, 10)),
       ('are', (11, 14)),
       ('you', (16, 19)),
       ('?', (19, 20))]
      
      In [10]: sent[14:16]
      Out[10]: '  '
      ```
      Note that there are actually two spaces in between `"are"` and `"you"`. The offsets reflect or keep track of that.

