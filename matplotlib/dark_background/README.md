```python
plt.style.use('dark_background')
```
cf. [https://matplotlib.org/gallery/style_sheets/dark_background.html#sphx-glr-gallery-style-sheets-dark-background-py](https://matplotlib.org/gallery/style_sheets/dark_background.html#sphx-glr-gallery-style-sheets-dark-background-py)


## Dark Reader
Some people like to read documents in dark/night mode, even with jupyter notebook. The `Dark Reader` from google add-ons is one such tools.

Usual `matplotlib` settings are not perfectly suited for such dark mode. The following code snippet can help to improve this respect. Feel
free to copy and paste it :)

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

DARK_READER = True
if DARK_READER:
    plt.rcParams.update({
        "lines.color": "white",
        "patch.edgecolor": "white",
        "text.color": "black",
        "axes.facecolor": "black",
        "axes.edgecolor": "lightgray",
        "axes.labelcolor": "white",
        "axes.titlecolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "lightgray",
        "figure.facecolor": "black",
        "figure.edgecolor": "black",
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black",
    })
```



