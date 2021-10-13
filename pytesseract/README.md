## Preliminaries
`pytesseract` is just a wrapper for `tesseract`. In Unix-like systems, the command line program `tesseract` can be installed
via the packages managers `apt, pacman, dnf, brew`, etc., depending on the distro in use.

For example, on Fedora, one installs `tesseract` as follows.
```bash
dnf install tesseract
# In order to detect other languages, e.g. Japanese, install
dnf install tesseract-langpack-jpn
```

Once `tesseract` installed, the installation of `pytesseract` is just ordinary `pip install pytesseract` or `conda install -n env_name pytesseract`.


