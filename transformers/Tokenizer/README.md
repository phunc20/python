## Btw Tokens and Token IDs
We call
- conversion from token to token ID: Encoding
    - Methods related to encoding includes `encode, __call__`
      ```python
      In [24]: sents = [
          ...:     'vì_vậy, thật thú_vị khi có_thể chứng_kiến sự_kiện và may_mắn là nó xảy ra khi trạm insight đang ghi lại dữ_liệu địa_chấn
          ...:  ".',
          ...:     'quan_điểm của tôi là cứ bền, rẻ, hợp sở_thích là mua.',
          ...:     'một xã_hội đáng sống đơn_giản là nơi ai cũng có cơ_hội được làm người bình_thường.',
          ...:     'lớp men mỏng tráng phủ trên bề_mặt được in hoa_văn với màu_sắc kích_thước khác nhau.',
          ...: ]
      
      In [25]: print(vi_tokenizer.encode(sents[0]))
      [0, 48093, 46924, 1581, 4, 520, 1748, 26, 62, 1590, 776, 6, 1309, 8, 231, 254, 40, 26, 1177, 1949, 4102, 9842, 52, 701, 44, 1470, 15789, 30939, 5, 2]
      
      In [26]: vi_tokenizer(sents)
      Out[26]: {'input_ids': [[0, 48093, 46924, 1581, 4, 520, 1748, 26, 62, 1590, 776, 6, 1309, 8, 231, 254, 40, 26, 1177, 1949, 4102, 9842, 52, 701, 44, 1470, 15789, 30939, 5, 2], [0, 1233, 7, 70, 8, 658, 56101, 1301, 4, 33462, 4, 2288, 4328, 8, 5301, 12584, 2], [0, 16, 267, 463, 235, 972, 8, 189, 277, 32, 10, 521, 11, 47, 18, 58054, 32678, 10838, 2], [0, 459, 4234, 2725, 11166, 2149, 34, 4336, 11, 858,
      9279, 15, 1921, 2481, 85, 2008, 4363, 5, 2]], 'token_type_ids': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]}
      ```
    - Note that `encode` is supposed to **apply only on one single string**, not a batch of strings.
      ```python
      In [27]: print(vi_tokenizer.encode(sents))  # This gives non-sense
      [0, 3, 3, 3, 3, 2]
      ```
      It is `__call__`'s job to encode batches.
- conversion from token ID to token: Decoding
    - Methods related to decoding includes `decode, batch_decode`
    - As the name suggests, `decode` can only be used to decode a single instance,
      i.e. a single token ID vector:
      ```python
      In [28]: import numpy as np
      
      In [29]: a = np.array([[    0,  1699,     4,   520,  1748,    26,    62,  1590,   776,
          ...:                    6,  1309,     8,   231,   254,    40,    26,  1177,  1949,
          ...:                 4102,  9842,    52,   701,    44,  1470, 15789,    22,     5],
          ...:               [    0,  1233,     7,    70,     8,   658,  6165,     4,  1455,
          ...:                    4,  2288,  4328,     8,   188,     5,     2,     1,     1,
          ...:                    1,     1,     1,     1,     1,     1,     1,     1,     1],
          ...:               [    0,    16,   267,   463,   235,   972,     8,   189,   277,
          ...:                   32,    10,   521,    11,    47,    18,  1006,     5,     2,
          ...:                    1,     1,     1,     1,     1,     1,     1,     1,     1],
          ...:               [    0,   459,  4234,  2725, 11166,  2149,    34,  4336,    11,
          ...:                  858,  9279,    15,  1921,  2481,    85,   138,     5,     2,
          ...:                    1,     1,     1,     1,     1,     1,     1,     1,     1]])
          ...:
      
      In [30]: from transformers import AutoTokenizer
      
      In [31]: vi_tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
      Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
      
      In [32]: vi_tokenizer.decode(a[0])
      Out[32]: '<s> vì_vậy, thật thú_vị khi có_thể chứng_kiến sự_kiện và may_mắn là nó xảy ra khi trạm insight đang ghi lại dữ_liệu địa_chấn ".'
      
      In [33]: vi_tokenizer.decode(a)
      TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
      
      In [34]: vi_tokenizer.batch_decode(a)
      Out[34]:
      ['<s> vì_vậy, thật thú_vị khi có_thể chứng_kiến sự_kiện và may_mắn là nó xảy ra khi trạm insight đang ghi lại dữ_liệu địa_chấn ".',
       '<s> quan_điểm của tôi là cứ bền, rẻ, hợp sở_thích là mua. </s> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad>',
       '<s> một xã_hội đáng sống đơn_giản là nơi ai cũng có cơ_hội được làm người bình_thường. </s> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad>',
       '<s> lớp men mỏng tráng phủ trên bề_mặt được in hoa_văn với màu_sắc kích_thước khác nhau. </s> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad> <pad>']
      ```
    - The Boolean arg `skip_special_tokens` could be used to specify whether we
      want special tokens like BOS token, UNK token, etc. to appear in the return
      value
      ```python
      In [35]: vi_tokenizer.decode(a[0], skip_special_tokens=True)
      Out[35]: 'vì_vậy, thật thú_vị khi có_thể chứng_kiến sự_kiện và may_mắn là nó xảy ra khi trạm insight đang ghi lại dữ_liệu địa_chấn ".'
      
      In [36]: vi_tokenizer.batch_decode(a, skip_special_tokens=True)
      Out[36]:
      ['vì_vậy, thật thú_vị khi có_thể chứng_kiến sự_kiện và may_mắn là nó xảy ra khi trạm insight đang ghi lại dữ_liệu địa_chấn ".',
       'quan_điểm của tôi là cứ bền, rẻ, hợp sở_thích là mua.',
       'một xã_hội đáng sống đơn_giản là nơi ai cũng có cơ_hội được làm người bình_thường.',
       'lớp men mỏng tráng phủ trên bề_mặt được in hoa_văn với màu_sắc kích_thước khác nhau.']
      ```






sents = [
    'vì_vậy, thật thú_vị khi có_thể chứng_kiến sự_kiện và may_mắn là nó xảy ra khi trạm insight đang ghi lại dữ_liệu địa_chấn ".',
    'quan_điểm của tôi là cứ bền, rẻ, hợp sở_thích là mua.',
    'một xã_hội đáng sống đơn_giản là nơi ai cũng có cơ_hội được làm người bình_thường.',
    'lớp men mỏng tráng phủ trên bề_mặt được in hoa_văn với màu_sắc kích_thước khác nhau.',
]
