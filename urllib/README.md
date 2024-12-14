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
