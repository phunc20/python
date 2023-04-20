## Bug(s)
- 2023/04/20
    - Certain sentences one cannot `add_accents` to them, e.g.
      ```python
      In [1]: from pyvi import ViUtils
      
      In [2]: s = "suy nghi rieng"
      
      In [3]: ViUtils.add_accents(s)
      ---------------------------------------------------------------------------
      KeyError                                  Traceback (most recent call last)
      Cell In[3], line 1
      ----> 1 ViUtils.add_accents(s)
      
      File ~/.config/miniconda3/envs/fraud/lib/python3.8/site-packages/pyvi/ViUtils.py:22, in add
      _accents(s)
           21 def add_accents(s):
      ---> 22     return ViDiac.add_accents(s)
      
      File ~/.config/miniconda3/envs/fraud/lib/python3.8/site-packages/pyvi/ViDiac.py:203, in add
      _accents(s)
          202 def add_accents(s):
      --> 203     return ViDiac.doit(s)
      
      File ~/.config/miniconda3/envs/fraud/lib/python3.8/site-packages/pyvi/ViDiac.py:199, in ViD
      iac.doit(str_sentence)
          197             unichar = unichar.upper()
          198         # print unichar
      --> 199         output += ViDiac.reversed_mapping[unichar]
          200 return output
      
      KeyError: 'ewx'
      ```
      If one **reads into the source code** or **tries to debug** (say, using `ipdb`),
      one'd find the cause being that the dictionary
      `ViDiac.reversed_mapping` lacks certain keys that `label` could produce.
      
      W/o diving into the inner working and design of the code, a quick bug fix could
      be
      ```python
      output += ViDiac.reversed_mapping.get(unichar, unichar[0])
      ```
      After such modification, we'd obtain
      ```python
      In [1]: from pyvi import ViDiac

      In [2]: ViDiac.ViDiac.doit("suy nghi rieng")
      Out[2]: 'Suy nghi rieng'
      
      In [3]: ViDiac.ViDiac.doit("suy nghi")
      Out[3]: 'Suy nghi'
      
      In [4]: ViDiac.ViDiac.doit("Mot nguoi co suy nghi.")
      Out[4]: 'Một người có suy nghĩ.'
      ```





