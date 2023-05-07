## Open Image Files
- **Using a for loop through the file handle** allows to load
  the file content into RAM **one line at a time**; in case of
  large, multi-line files, this could be a way to avoid exhausting
  RAM.  
  
  For example, the following code creates a multi-line file of
  about 4GB filesize
  ```python
  In [19]: line = "0"*(2**20)  # About 1M
      ...: with open("lots_zeros", "w", encoding="utf-8") as f:
      ...:     n_lines = 4*(2**10)
      ...:     for _ in tqdm(range(n_lines)):
      ...:         f.write(f'{line}\n')
      ...:
  100%|█████████████████████████████████████████████████| 4096/4096 [00:32<00:00, 126.35it/s]
  ```
  One could compare the following two code snippets' RAM usage by opening
  some kind of RAM monitor (e.g. on Linux command line with `$ watch -n .5 free -m`)
  ```python
  # Memory hog
  with open("lots_zeros", "r", encoding="utf-8") as f:
      content = f.read()
  n_chars = len(content)

  # Reading into memory one line at a time
  n_chars = 0
  with open("lots_zeros", "r", encoding="utf-8") as f:
      for line in f:
        n_chars += len(line)
  ```
    - Fun fact: `4.0K` seems to be the minimum size of a text file in Linux;
      or more "correctly", `4.0K` is the unit of file size in Linux, i.e.
      file size steps from `4.0K` to `8.0K` to ..., and so on.
      ```python
      In [1]: line = "0"*(2**10)
        ...: with open("lots_zeros", "w", encoding="utf-8") as f:
        ...:     n_lines = 1
        ...:     for _ in range(n_lines):
        ...:         f.write(f'{line}\n')
        ...:
      
      In [2]: !du -hsx lots_zeros
      4.0K    lots_zeros
      
      In [3]: line = "0"*(1)
         ...: with open("lots_zeros", "w", encoding="utf-8") as f:
         ...:     n_lines = 1
         ...:     for _ in range(n_lines):
         ...:         f.write(f'{line}\n')
         ...:
      
      In [4]: !du -hsx lots_zeros
      4.0K    lots_zeros

      In [5]: line = "0"*(4*2**10-1)
         ...: with open("lots_zeros", "w", encoding="utf-8") as f:
         ...:     n_lines = 1
         ...:     for _ in range(n_lines):
         ...:         f.write(f'{line}\n')
         ...:
      
      In [6]: !du -hsx lots_zeros
      4.0K    lots_zeros
      
      In [7]: line = "0"*(4*2**10)
         ...: with open("lots_zeros", "w", encoding="utf-8") as f:
         ...:     n_lines = 1
         ...:     for _ in tqdm(range(n_lines)):
         ...:         f.write(f'{line}\n')
         ...:
      100%|█████████████████████████████████████████████████████| 1/1 [00:00<00:00, 11008.67it/s]
      
      In [8]: !du -hsx lots_zeros
      8.0K    lots_zeros
      ```
- To open a binary file, one must use `"rb"`
  (which stands for "read" and "binary") instead of simply `"r"`
  - `"br"` is ok, too. (i.e. the order does not matter)
  ```
  In [47]: path_imagefile = Path("/home/phunc20/datasets/t-brain/chinese_handwrite/train/48705_裕.jpg")
  
  In [48]: path_textfile = Path("/home/phunc20/vol.md")
  
  In [49]: with open(path_imagefile, "r") as f:
      ...:     content = f.read()
      ...:
      ...:
  ---------------------------------------------------------------------------
  UnicodeDecodeError                        Traceback (most recent call last)
  <ipython-input-49-467006bdf8e4> in <module>
        1 with open(path_imagefile, "r") as f:
  ----> 2     content = f.read()
        3
        4
  
  ~/.config/miniconda3/envs/oft/lib/python3.7/codecs.py in decode(self, input, final)
      320         # decode input (taking the buffer into account)
      321         data = self.buffer + input
  --> 322         (result, consumed) = self._buffer_decode(data, self.errors, final)
      323         # keep undecoded input until the next call
      324         self.buffer = data[consumed:]
  
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
  
  In [50]: with open(path_imagefile, "rb") as f:
      ...:     content = f.read()
      ...:
  
  In [51]: content
  Out[51]: b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06...'
  
  In [56]: type(content)
  Out[56]: bytes
  
  In [52]: with open(path_textfile, "r") as f:
      ...:     content = f.read()
      ...:
  
  In [53]: content
  Out[53]: '4.0K\tanimal.sql\n4.0K\tDownloads\n4.0K\tsd-card\n8.0K\tDesktop\n12K\tArduino\n56K\thw2.jl\n364K\tscikit_learn_data\n596K\ttodo\n648K\tbrowser-tabs\n11M\tgo\n27M\tpictures\n79M\tmusic\n457M\tjobs\n1.8G\tcorbeille\n2.5G\tbiblio\n6.6G\tgit-repos\n7.6G\tcell-phones\n21G\tdatasets\n24G\tmooc\n38G\tdownloads\n207G\tvideos\n'
  
  In [56]: type(content)
  Out[56]: str
  
  In [54]: with open(path_textfile, "br") as f:
      ...:     content = f.read()
  
  In [55]: content
  Out[55]: b'4.0K\tanimal.sql\n4.0K\tDownloads\n4.0K\tsd-card\n8.0K\tDesktop\n12K\tArduino\n56K\thw2.jl\n364K\tscikit_learn_data\n596K\ttodo\n648K\tbrowser-tabs\n11M\tgo\n27M\tpictures\n79M\tmusic\n457M\tjobs\n1.8G\tcorbeille\n2.5G\tbiblio\n6.6G\tgit-repos\n7.6G\tcell-phones\n21G\tdatasets\n24G\tmooc\n38G\tdownloads\n207G\tvideos\n'
  
  In [56]: type(content)
  Out[56]: bytes
  ```



