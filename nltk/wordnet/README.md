


```python
In [1]: import nltk

In [2]: nltk.download("wordnet")
[nltk_data] Downloading package wordnet to /home/phunc20/nltk_data...
[nltk_data]   Unzipping corpora/wordnet.zip.
Out[2]: True

In [3]: nltk.download("omw-1.4")
[nltk_data] Downloading package omw-1.4 to /home/phunc20/nltk_data...
[nltk_data]   Unzipping corpora/omw-1.4.zip.
Out[3]: True

In [4]: from nltk.corpus import wordnet

In [5]: wordnet.synsets("car")
Out[5]:
[Synset("car.n.01"),
 Synset("car.n.02"),
 Synset("car.n.03"),
 Synset("car.n.04"),
 Synset("cable_car.n.01")]

In [6]: car1 = wordnet.synset("car.n.01"); car1.definition()
Out[6]: 'a motor vehicle with four wheels; usually propelled by an internal combustion engine'

In [7]: [syn.definition() for syn in wordnet.synsets("car")]
Out[7]:
['a motor vehicle with four wheels; usually propelled by an internal combustion engine',
 'a wheeled vehicle adapted to the rails of railroad',
 'the compartment that is suspended from an airship and that carries personnel and the cargo and the power plant',
 'where passengers ride up and down',
 'a conveyance for passengers or freight on a cable railway']

In [8]: wordnet.synset("car.n.01") is wordnet.synsets("car")[0]
Out[8]: True




```
