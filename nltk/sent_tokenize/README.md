```
In [1]: import sys

In [2]: sys.version
Out[2]: '3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0]'

In [3]: import nltk
   ...: from nltk.tokenize import sent_tokenize
   ...:
   ...: # This data is needed to enable English sentence tokenization
   ...: nltk.download("punkt_tab")
[nltk_data] Downloading package punkt_tab to
[nltk_data]     /home/phunc20/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt_tab.zip.
Out[2]: True

In [3]: !tree -a ~/nltk_data
/home/phunc20/nltk_data
└── tokenizers
    ├── punkt_tab
    │   ├── czech
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── danish
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── dutch
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── english
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── estonian
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── finnish
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── french
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── german
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── greek
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── italian
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── norwegian
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── polish
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── portuguese
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── README
    │   ├── russian
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── slovene
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── spanish
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   ├── swedish
    │   │   ├── abbrev_types.txt
    │   │   ├── collocations.tab
    │   │   ├── ortho_context.tab
    │   │   └── sent_starters.txt
    │   └── turkish
    │       ├── abbrev_types.txt
    │       ├── collocations.tab
    │       ├── ortho_context.tab
    │       └── sent_starters.txt
    └── punkt_tab.zip

21 directories, 74 files

In [4]: long_text = """
   ...:    Mr. Rabbit sat on his front porch rocking, eating a great big carrot,
   ...: and looking.
   ...:
   ...:    "Looks like Sly Fox coming down the road," he said to himself, walking
   ...: to the end of the porch. Shading his eyes with his paws, he exclaimed, "It
   ...: is Sly Fox."
   ...:
   ...:    "Good morning Mr. Rabbit," cried Sly Fox, as he walked across the yard.
   ...: "Good morning," replied Mr. Rabbit, a slight frown on his face.
   ...:
   ...:    "Well," said Sly Fox, "as I haven't seen you in so long a time, thought
   ...: I would stop and chat a while."
   ...:
   ...:    Mr. Rabbit could not be rude in his own home, even to an enemy, so he
   ...: offered Sly Fox a seat on the porch.
   ...:
   ...:    "Take a chair," he said politely. But Sly Fox did not stay long, and as
   ...: he was leaving, he asked: "Mr. Rabbit, my mother is having a good dinner
   ...: tonight. Won't you, Mrs. Rabbit, and your three little rabs come to dinner
   ...: with me?"
   ...: """

In [5]: chunks = sent_tokenize(long_text)

In [6]: chunks
Out[6]:
['\n    Mr. Rabbit sat on his front porch rocking, eating a great big carrot,\nand looking.',
 '"Looks like Sly Fox coming down the road," he said to himself, walking\nto the end of the porch.',
 'Shading his eyes with his paws, he exclaimed, "It\nis Sly Fox."',
 '"Good morning Mr. Rabbit," cried Sly Fox, as he walked across the yard.',
 '"Good morning," replied Mr. Rabbit, a slight frown on his face.',
 '"Well," said Sly Fox, "as I haven\'t seen you in so long a time, thought\nI would stop and chat a while."',
 'Mr. Rabbit could not be rude in his own home, even to an enemy, so he\noffered Sly Fox a seat on the porch.',
 '"Take a chair," he said politely.',
 'But Sly Fox did not stay long, and as\nhe was leaving, he asked: "Mr. Rabbit, my mother is having a good dinner\ntonight.',
 'Won\'t you, Mrs. Rabbit, and your three little rabs come to dinner\nwith me?"']
```

- To be able to tokenize English sentences, one needs to `nltk.download("punkt_tab")`
    - This defaults to downloading to `~/nltk_data/`.
    - Note that after decompress the `punkt_tab.zip` file,
      Python does not delete the zip file.
- `sent_tokenize`
    - its input is a string
    - its output is a list of strings/sentences.
