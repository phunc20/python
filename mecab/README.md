
- <https://github.com/SamuraiT/mecab-python3>
- <https://taku910.github.io/mecab/>
- <https://github.com/taku910/mecab>
- <https://github.com/chezou/MeCab.jl>

## Installation
01. Create a new env, here named `mecab`, and activate it.
02. `pip install mecab-python3` into that env
03. At this point if you try to run the following code, you should meet the same error/exception.
    ```
    (mecab) ~ ❯❯❯ ipython
    Python 3.7.9 (default, Dec 18 2020, 00:08:56)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.25.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: import MeCab
    
    In [2]: wakati = MeCab.Tagger("-Owakati")
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    ~/.virtualenvs/mecab/lib/python3.7/site-packages/MeCab/__init__.py in __init__(self, rawargs)
        132         try:
    --> 133             super(Tagger, self).__init__(args)
        134         except RuntimeError as ee:
    
    RuntimeError:
    
    The above exception was the direct cause of the following exception:
    
    RuntimeError                              Traceback (most recent call last)
    <ipython-input-2-d5a1c2f04796> in <module>
    ----> 1 wakati = MeCab.Tagger("-Owakati")
    
    ~/.virtualenvs/mecab/lib/python3.7/site-packages/MeCab/__init__.py in __init__(self, rawargs)
        133             super(Tagger, self).__init__(args)
        134         except RuntimeError as ee:
    --> 135             raise RuntimeError(error_info(rawargs)) from ee
        136
        137
    
    RuntimeError:
    ----------------------------------------------------------
    
    Failed initializing MeCab. Please see the README for possible solutions:
    
        https://github.com/SamuraiT/mecab-python3#common-issues
    
    If you are still having trouble, please file an issue here, and include the
    ERROR DETAILS below:
    
        https://github.com/SamuraiT/mecab-python3/issues
    
    issueを英語で書く必要はありません。
    
    ------------------- ERROR DETAILS ------------------------
    arguments: -Owakati
    [ifs] no such file or directory: /usr/local/etc/mecabrc
    ----------------------------------------------------------
    ```
    The `-Owakati`'s `-O` mean _Output_.
04. As the error message indicated, it suffices to go to the GitHub page and following the instructions. In this case, we are missing a dictionary, so we `pip install unidic-lite`. After that, the demo code should run fine.
    ```
    In [3]: !pip install unidic-lite
    Collecting unidic-lite
      Downloading unidic-lite-1.0.8.tar.gz (47.4 MB)
         |████████████████████████████████| 47.4 MB 174 kB/s
    Building wheels for collected packages: unidic-lite
      Building wheel for unidic-lite (setup.py) ... done
      Created wheel for unidic-lite: filename=unidic_lite-1.0.8-py3-none-any.whl size=47658837 sha256=76d2d16d1734a2ffabb60f49f1abfffbe0fa70f8b35ba299b5ee58d014ffea88
      Stored in directory: /home/phunc20/.cache/pip/wheels/de/69/b1/112140b599f2b13f609d485a99e357ba68df194d2079c5b1a2
    Successfully built unidic-lite
    Installing collected packages: unidic-lite
    Successfully installed unidic-lite-1.0.8
    WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
    You should consider upgrading via the '/home/phunc20/.virtualenvs/mecab/bin/python -m pip install --upgrade pip' command.
    
    In [4]: wakati = MeCab.Tagger("-Owakati")
    
    In [5]: wakati.parse("pythonが大好きです").split()
    Out[5]: ['python', 'が', '大好き', 'です']
    
    In [6]: wakati.parse("pythonが大好きです")
    Out[6]: 'python が 大好き です \n'
    
    In [7]: tagger = MeCab.Tagger()
    
    In [8]: tagger.parse("pythonが大好きです")
    Out[8]: 'python\tpython\tpython\tpython\t名詞-普通名詞-一般\t\t\t0\nが\tガ\tガ\tが\t助詞-格助詞\t\t\t\n大好き\tダイスキ\tダイスキ\t大好き\t形状詞-一般\t\t\t1\nです\tデス\tデス\tです\t助動詞\t助動詞-デス\t終止形-一般\t\nEOS\n'
    
    In [9]: print(tagger.parse("pythonが大好きです"))
    python  python  python  python  名詞-普通名詞-一般                      0
    が      ガ      ガ      が      助詞-格助詞
    大好き  ダイスキ        ダイスキ        大好き  形状詞-一般                     1
    です    デス    デス    です    助動詞  助動詞-デス     終止形-一般
    EOS
    
    
    In [10]: print(tagger.parse("issueを英語で書く必要はありません。"))
    issue   issue   issue   issue   名詞-普通名詞-一般                      0
    を      オ      ヲ      を      助詞-格助詞
    英語    エーゴ  エイゴ  英語    名詞-普通名詞-一般                      0
    で      デ      デ      で      助詞-格助詞
    書く    カク    カク    書く    動詞-一般       五段-カ行       連体形-一般     1
    必要    ヒツヨー        ヒツヨウ        必要    名詞-普通名詞-形状詞可能                        0
    は      ワ      ハ      は      助詞-係助詞
    あり    アリ    アル    有る    動詞-非自立可能 五段-ラ行       連用形-一般     1
    ませ    マセ    マス    ます    助動詞  助動詞-マス     未然形-一般
    ん      ン      ズ      ず      助動詞  助動詞-ヌ       終止形-撥音便
    。                      。      補助記号-句点
    EOS
    
    
    In [11]: wakati.parse("issueを英語で書く必要はありません。")
    Out[11]: 'issue を 英語 で 書く 必要 は あり ませ ん 。 \n'
    
    In [12]:
    ```
  - Note that the `wakati` parser above add spaces to the sentences, wherease `tagger.parse()` add a whole bunch of other stuffs.


```python
In [1]: import MeCab

In [2]: wakati = MeCab.Tagger("-Owakati")

In [3]: wakati.parse("issueを英語で書く必要はありません。")
Out[3]: 'issue を 英語 で 書く 必要 は あり ませ ん 。 \n'

In [4]: wakati.parse("issueを英語で書く必要はありません。").split()
Out[4]: ['issue', 'を', '英語', 'で', '書く', '必要', 'は', 'あり', 'ませ', 'ん', '。']

In [5]: wakati.parse("pythonが大好きです").split()
Out[5]: ['python', 'が', '大好き', 'です']

In [6]: tagger = MeCab.Tagger()

In [7]: tagger.parse("pythonが大好きです")
Out[7]: 'python\tpython\tpython\tpython\t名詞-普通名詞-一般\t\t\t0\nが\tガ\tガ\tが\t助詞-格
助詞\t\t\t\n大好き\tダイスキ\tダイスキ\t大好き\t形状詞-一般\t\t\t1\nです\tデス\tデス\tです\
t助動詞\t助動詞-デス\t終止形-一般\t\nEOS\n'

In [8]: print(tagger.parse("pythonが大好きです"))
python  python  python  python  名詞-普通名詞-一般                      0
が      ガ      ガ      が      助詞-格助詞
大好き  ダイスキ        ダイスキ        大好き  形状詞-一般                     1
です    デス    デス    です    助動詞  助動詞-デス     終止形-一般
EOS


In [9]: print(tagger.parse("issueを英語で書く必要はありません。"))
issue   issue   issue   issue   名詞-普通名詞-一般                      0
を      オ      ヲ      を      助詞-格助詞
英語    エーゴ  エイゴ  英語    名詞-普通名詞-一般                      0
で      デ      デ      で      助詞-格助詞
書く    カク    カク    書く    動詞-一般       五段-カ行       連体形-一般     1
必要    ヒツヨー        ヒツヨウ        必要    名詞-普通名詞-形状詞可能                  0
は      ワ      ハ      は      助詞-係助詞
あり    アリ    アル    有る    動詞-非自立可能 五段-ラ行       連用形-一般     1
ませ    マセ    マス    ます    助動詞  助動詞-マス     未然形-一般
ん      ン      ズ      ず      助動詞  助動詞-ヌ       終止形-撥音便
。                      。      補助記号-句点
EOS


In [10]:
```


