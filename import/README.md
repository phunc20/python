
What's the diff btw the following?
- `import <some_package>`
- `from <some_package> import *`
  - **(R)** Ageron said that this only imports things from `<some_package>.__all__`
```ipython
In [1]: import sklearn

In [2]: "tree" in sklearn.__all__
Out[2]: True

In [3]: "datasets" in sklearn.__all__
Out[3]: True

In [4]: sklearn.tree
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-4-1bb4d32979dc> in <module>
----> 1 sklearn.tree

AttributeError: module 'sklearn' has no attribute 'tree'

In [5]: from sklearn import *

In [6]: sklearn.tree
Out[6]: <module 'sklearn.tree' from '/home/phunc20/.virtualenvs/homl1e/lib/python3.7/site-packages/sklearn/tree/__init__.py'>

In [7]: tree
Out[7]: <module 'sklearn.tree' from '/home/phunc20/.virtualenvs/homl1e/lib/python3.7/site-packages/sklearn/tree/__init__.py'>

In [8]: dir(sklearn)
Out[8]:
['__SKLEARN_SETUP__',
 '__all__',
 '__builtins__',
 '__cached__',
 '__check_build',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 '__version__',
 '_config',
 '_distributor_init',
 '_isotonic',
 '_loss',
 'base',
 'calibration',
 'clone',
 'cluster',
 'compose',
 'config_context',
 'covariance',
 'cross_decomposition',
 'datasets',
 'decomposition',
 'discriminant_analysis',
 'dummy',
 'ensemble',
 'exceptions',
 'experimental',
 'externals',
 'feature_extraction',
 'feature_selection',
 'gaussian_process',
 'get_config',
 'impute',
 'inspection',
 'isotonic',
 'kernel_approximation',
 'kernel_ridge',
 'linear_model',
 'logger',
 'logging',
 'manifold',
 'metrics',
 'mixture',
 'model_selection',
 'multiclass',
 'multioutput',
 'naive_bayes',
 'neighbors',
 'neural_network',
 'os',
 'pipeline',
 'preprocessing',
 'random',
 'random_projection',
 'semi_supervised',
 'set_config',
 'setup_module',
 'show_versions',
 'svm',
 'sys',
 'tree',
 'utils']

```
