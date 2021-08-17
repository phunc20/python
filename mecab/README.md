
- <https://github.com/SamuraiT/mecab-python3>
- <https://taku910.github.io/mecab/>
- <https://github.com/taku910/mecab>
- <https://github.com/chezou/MeCab.jl>


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


