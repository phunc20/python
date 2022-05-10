import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix


label_list = [
    "rabbit",
    "bird",
    "tigre",
    "elephant",
    "cat",
]

def conf_mx_fig(
        conf_mx,
        label_list,
        title,
        num_in_cell=False,
        figsize=[10, 9],
        fontsize=8,
        cmap=plt.cm.gray):
    fig = plt.figure(figsize=figsize)
    ax = fig.gca()
    ax.set_title(title)
    ax.set_ylabel("True label")
    ax.set_yticks(
        range(len(label_list)),
        labels=label_list,
        fontsize=fontsize,
    )
    ax.set_xlabel("Predicted label")
    ax.set_xticks(
        range(len(label_list)),
        labels=label_list,
        fontsize=fontsize,
        horizontalalignment="right",
        rotation_mode="anchor",
        rotation=30,
    )
    ax.matshow(conf_mx, cmap=cmap)
    ax.tick_params(labelbottom=True, labeltop=False, top=False)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))

    # Add number display in each cell
    if num_in_cell:
        kw = dict(horizontalalignment="center",
                  verticalalignment="center")
        textcolors=("white", "black")
        valfmt = matplotlib.ticker.StrMethodFormatter("{x:0d}")
        threshold = (conf_mx.max()+conf_mx.min()) / 2
        for i in range(conf_mx.shape[0]):
            for j in range(conf_mx.shape[1]):
                kw.update(color=textcolors[int(conf_mx[i, j] > threshold)])
                text = ax.text(j, i, valfmt(conf_mx[i, j], None), **kw)

    return fig

n_samples = 1_000
y_true = np.random.choice(label_list, n_samples)
y_pred = np.random.choice(label_list, n_samples)

conf_mx = confusion_matrix(y_true, y_pred, labels=label_list)
fig_conf_mx = conf_mx_fig(conf_mx, label_list, "Confusion Matrix", num_in_cell=True)

row_sums = conf_mx.sum(axis=1, keepdims=True)
# to avoid division by zero
row_sums[row_sums == 0] = 1
rel_err = conf_mx / row_sums
# making the diagonal visually standout when there are many labels
#np.fill_diagonal(rel_err, 1)
np.fill_diagonal(rel_err, 0)
fig_rel_err = conf_mx_fig(rel_err, label_list, "Relative Error")

plt.show()
#plt.show(block=False)
