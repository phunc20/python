- [UTF-8 encoded bytes escaped with URL quoting](https://stackoverflow.com/questions/16566069/url-decode-utf-8-in-python)

  ```ipython
  In [1]: import urllib
  
  In [2]: urllib.parse.unquote("%E8%AE%80%E6%AA%94%E6%A1%88%E5%8F%8D%E8%80%8C%E6%AF%94%E8%BC%83%E6%85%A2")
  Out[2]: '讀檔案反而比較慢'
  ```

  Conversely, we've got `urllib.parse.quote`:

  ```ipython
  In [1]: from urllib.parse import quote
  
  In [2]: quote("日本語教育")
  Out[2]: '%E6%97%A5%E6%9C%AC%E8%AA%9E%E6%95%99%E8%82%B2'
  ```

  Related functions include `parse_qs` and `parse_qsl`, the former returning a `dict`,
  the latter a `list`:

  ```ipython
  In [4]: query = 'name=Rajeev+Singh&phone=%2B919999999999&phone=%2B628888888888'
  
  In [5]: from urllib.parse import parse_qs, parse_qsl
  
  In [6]: parse_qs(query)
  Out[6]: {'name': ['Rajeev Singh'], 'phone': ['+919999999999', '+628888888888']}
  
  In [7]: parse_qsl(query)
  Out[7]:
  [('name', 'Rajeev Singh'),
   ('phone', '+919999999999'),
   ('phone', '+628888888888')]
  ```

- Instead of being similar to `"/".join([base, url])`,
  `urllib.parse.urljoin(base, url)` seems to be more like `"".join([base, url])`:
  ```bash
  $ ipython
  Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:12:24) [GCC 11.2.0]
  Type 'copyright', 'credits' or 'license' for more information
  IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.
  
  In [1]: import urllib
  
  In [2]: urllib.parse.urljoin("https://translate.google.com/m", "?sl=en&tl=de&g=I don't know.")
  Out[2]: "https://translate.google.com/m?sl=en&tl=de&g=I don't know."
  
  In [3]: urllib.parse.urljoin("https://translate.google.com/m/", "?sl=en&tl=de&g=I don't know.")
  Out[3]: "https://translate.google.com/m/?sl=en&tl=de&g=I don't know."
  ```
- Download files using `urllib`
    - To write the response into a file, one needs to **write the bytes**, i.e. `"wb"`, instead of `"w"`. E.g.
        - Some GitHub file
          ```python
          url = "https://github.com/taborlab/FlowCal/raw/master/examples/FCFiles/sample001.fcs"
          with urllib.request.urlopen(url) as response:
              saved_path = Path.cwd()/url.split("/")[-1]
              with open(saved_path, "wb") as f:
                  f.write(response.read())
              print(f'Finish downloading {saved_path}')
          ```
        - MNIST test set
          ```python
          mnist_url = "http://yann.lecun.com/exdb/mnist/"
          test_set_gzip = "t10k-images-idx3-ubyte.gz"
          mnist_test_set_url = mnist_url + test_set_gzip
          with urllib.request.urlopen(mnist_test_set_url) as response:
              mnist_path = Path.cwd()/mnist_test_set_url.split("/")[-1]
              with open(mnist_path, "wb") as f:
                  f.write(response.read())
              print(f'The gzip file is downloaded at {mnist_path.absolute()}')"
          ```
    - The URL should not contain space character. E.g.
      ```python
      In [1]: import urllib
      
      In [2]: BASE_URL = "https://translate.google.com/m"
      
      In [3]: source_lang_code = "en"
         ...: target_lang_code = "de"
         ...: text = "What you see is what you get."
         ...:
         ...: query_url = urllib.parse.urljoin(
         ...:     BASE_URL,
         ...:     f"?sl={source_lang_code}&tl={target_lang_code}&q={text}"
         ...: )
         ...: query_url
      Out[3]: 'https://translate.google.com/m?sl=en&tl=de&q=What you see is what you get.'
      
      In [4]: response = urllib.request.urlopen(query_url)
      ---------------------------------------------------------------------------
      InvalidURL                                Traceback (most recent call last)
      Cell In[4], line 1
      ----> 1 response = urllib.request.urlopen(query_url)
      
      File ~/.config/miniconda3/envs/py3.12/lib/python3.12/urllib/request.py:215, in urlopen(url, data, timeout, cafile, capath, cadefault, context)
          213 else:
          214     opener = _opener
      --> 215 return opener.open(url, data, timeout)
      
      InvalidURL: URL can't contain control characters. '/m?sl=en&tl=de&q=What you see is what you get.' (found at least ' ')
      
      In [5]: # https://en.wikipedia.org/wiki/Percent-encoding
         ...: # Either one will do
         ...: query_url = query_url.replace(" ", "+")
         ...: #query_url = query_url.replace(" ", "%20")
         ...:
         ...: response = urllib.request.urlopen(query_url)
      
      In [6]: response.status
      Out[6]: 200
      
      In [7]: html_str = response.read().decode()
      
      In [8]: print(html_str[-500:])
      ="Translate" class="translate-button"></div></form></div><div class="result-container">Was Sie sehen, ist, was Sie bekommen.</div><div class="links-container"><ul><li><a href="https://www.google.com/m?hl=en-US">Google home</a></li><li><a href="https://www.google.com/tools/feedback/survey/xhtml?productId=95112&hl=en-US">Send feedback</a></li><li><a href="https://www.google.com/intl/en-US/policies">Privacy and terms</a></li><li><a href="./full">Switch to full site</a></li></ul></div></body></html>
      
      In [9]:
      ```
