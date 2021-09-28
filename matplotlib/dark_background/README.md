```python
plt.style.use('dark_background')
```
cf. [https://matplotlib.org/gallery/style_sheets/dark_background.html#sphx-glr-gallery-style-sheets-dark-background-py](https://matplotlib.org/gallery/style_sheets/dark_background.html#sphx-glr-gallery-style-sheets-dark-background-py)


## Dark Reader
Some people like to read documents in dark/night mode, even with jupyter notebook. The `Dark Reader` from google add-ons is one such tool.

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

There seems to exist not only one way to do this:
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["grid.color"] = "w"
mpl.rcParams["axes.facecolor"] = "w"
mpl.rcParams["axes.edgecolor"] = "w"
mpl.rcParams["axes.titlecolor"] = "w"
mpl.rcParams["axes.labelcolor"] = "w"
mpl.rcParams["text.color"] = "w"
mpl.rcParams["xtick.color"] = "w"
mpl.rcParams["ytick.color"] = "w"

mpl.rcParams["axes.facecolor"] = "k"
mpl.rcParams["figure.facecolor"] = "k"
mpl.rcParams["figure.figsize"] = (8,6)
mpl.rcParams["axes.grid"] = False
```
