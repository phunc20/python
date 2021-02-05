As of 2021/02/05, I've encountered several times the situation where autocompletion of Python
code was not working. According to [this stackoverflow post](https://stackoverflow.com/questions/33665039/tab-completion-does-not-work-in-jupyter-notebook-but-fine-in-ipython-terminal),
it seemed to be an issue of `jedi` and it recommended installing `pip install jedi==0.17.2`

**Rmk.** In miniconda, one does
```bash
# To check the installed jedi version inside environment <env>
conda list -n <env> | grep jedi
# To install the right version of jedi inside environment <env>
conda install -n <env> jedi=0.17.2
# Note that conda uses only one equal sign whereas pip two equal signs.
```
