## Installation
- Since `pymupdf` is simply a wrapper around `mupdf`, different Linux distros need to install `mupdf` differently:
    - Fedora: `dnf install mupdf`
    - Arch Linux: `pacman -S mupdf`
- Then, to install, `pip install pymupdf`


## Usage
- `import fitz`, not `import pymupdf`. Cf. [here for the naming](https://github.com/pymupdf/PyMuPDF/wiki)
- Check version by `fitz.__doc__`, not by `fitz.__version__`, which does not even exist
- [OCR-like usage](https://pymupdf.readthedocs.io/en/latest/app1.html#blocks)


## Info Extraction
- Page dimension could be obtained by code like
  ```python
  In [1]: with fitz.open("linking.pdf") as doc:
     ...:     page = doc[0]
     ...:     print(f'{page.mediabox = }')
     ...:     print(f'{page.mediabox_size = }')
     ...:     print(f'{page.mediabox_size.x = }')
     ...:     print(f'{page.mediabox_size.y = }')
  page.mediabox = Rect(0.0, 0.0, 612.0, 792.0)
  page.mediabox_size = Point(612.0, 792.0)
  page.mediabox_size.x = 612.0
  page.mediabox_size.y = 792.0
  ```
  The `mediabox` bascially gives the information of `(x0,y0,x2,y2)`, i.e.
  the coordinates of the top left and the bottom right corners, which means
  that it's sensible to extract the dimension of the page as follows.
  ```python
  width = int(page.mediabox_size.x)
  height = int(page.mediabox_size.y)
  ```
- [Get text from real PDFs by `text = page.get_text(opt)`](https://pymupdf.readthedocs.io/en/latest/tutorial.html#extracting-text-and-images), where `opt` could be one of the following:
    - `"text"` (default)
    - `"blocks"`: Litterally, blocks of text. Usually `pymupdf` tends to think
      of as block whole chunk of text, thus including texts in consecutive lines
    - `"words"`: This is like `"blocks"` being processed by the string method `split`. However,
      one **usefulness** of this is that it also **takes care of the bbox info**.
    - `"html"`
    - `"dict"`
    - `"rawdict"`
    - `"xhtml"`
    - `"xml"`


