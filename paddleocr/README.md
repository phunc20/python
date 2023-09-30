## Diff Languages
Although traditional Chinese (i.e. `chinese_cht`) is supported, it seems that
simplified Chinese's (i.e. `ch`) model was better/more fully trained.
```python

```


## Running on Colab (2023/09/28, PaddlePaddle release 2.7)
### Package Installation
You might encounter the following error when you try to
`from paddleocr import PaddleOCR`:
```
Error: Can not import paddle core while this file exists: /usr/local/lib/python3.10/dist-packages/paddle/fluid/libpaddle.so

---------------------------------------------------------------------------

ImportError                               Traceback (most recent call last)

<ipython-input-3-b1e76e7b262b> in <cell line: 1>()
----> 1 from paddleocr import PaddleOCR, draw_ocr

8 frames

/usr/local/lib/python3.10/dist-packages/paddle/fluid/core.py in <module>
    267 
    268 try:
--> 269     from . import libpaddle
    270 
    271     if avx_supported() and not libpaddle.is_compiled_with_avx():

ImportError: libssl.so.1.1: cannot open shared object file: No such file or directory
```

Long story short:
1. aidsjf
2. aisdjif

tldr; every single clue I found on the Internet turned out to be no rescue
to this error:
1. [This StackOverflow post](https://stackoverflow.com/questions/76388016/error-can-not-import-paddle-core-while-this-file-exists)
   claims to solve the error by
   ```bash
   ! python -m pip install --force-reinstall paddlepaddle==2.5
   ```
   But it doesn't work for me on colab.
1. [This](https://stackoverflow.com/questions/76728440/not-able-to-import-paddleocr-library-on-google-colab),
   more plausibly tries to downgrade/install `libssl` to the specific version
   in the error message.
   ```bash
   !wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
   !sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb
   ```
1. Neither of these two github issues work in my case
    - <https://github.com/PaddlePaddle/Paddle/issues/48681>  
      I don't know how to `export` on colab
    - <https://github.com/PaddlePaddle/Paddle/issues/48667>  
      I cannot seem to find the file `libpython3.9.so.1.0` on colab --
      colab is not using conda
