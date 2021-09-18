## Experiment Preparation
```bash
(oft) python/zipfile/filename_encoding % ls
README.md      naive_unzip.py unzip.py
(oft) python/zipfile/filename_encoding % touch 日本やベトナム.txt
(oft) python/zipfile/filename_encoding % ls
README.md                 unzip.py
naive_unzip.py            日本やベトナム.txt
(oft) python/zipfile/filename_encoding % zip 日本やベトナム.txt.zip 日本やベトナム.txt
  adding: 日本やベトナム.txt (stored 0%)
(oft) python/zipfile/filename_encoding % ls
README.md                     unzip.py                      日本やベトナム.txt.zip
naive_unzip.py                日本やベトナム.txt
```


## Linux Command `unzip` and Python's `zipfile` Package's Behaviour
Filename with wrong encoding `µùÑµ£¼πéäπâÖπâêπâèπâá.txt` took place if special care is not taken.
```
(oft) python/zipfile/filename_encoding % unzip -d good 日本やベトナム.txt.zip
Archive:  日本やベトナム.txt.zip
 extracting: good/???????????.txt
(oft) python/zipfile/filename_encoding % ls good
日本やベトナム.txt
(oft) python/zipfile/filename_encoding % python naive_unzip.py 日本やベトナム.txt.zip -d bad
(oft) python/zipfile/filename_encoding % ls bad 
µùÑµ£¼πéäπâÖπâêπâèπâá.txt
(oft) python/zipfile/filename_encoding % python unzip.py 日本やベトナム.txt.zip -d fix
(oft) python/zipfile/filename_encoding % ls fix
日本やベトナム.txt
```

Cf. `./unzip.py` for more details.

**Rmk.** The above situation seems to only take place when one `touch` a Japanese-named file from MacOS, and then
tries to unzip it (in all Linux, Windows and MacOS) using the `naive_unzip.py` script.
I haven't figured out the reason, but I guess that it has sth to do with the encoding of Japanese in MacOS.
