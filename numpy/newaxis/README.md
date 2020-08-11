<b>Example 01</b>
<pre>
In [1]: import numpy as np

In [2]: np.zeros((3,4))[np.newaxis].shape
Out[2]: (1, 3, 4)

In [3]: np.zeros((3,4))[:, np.newaxis, :].shape
Out[3]: (3, 1, 4)
</pre>



<b>Example 02</b>
<pre>
def epsilon_greedy_policy(state, epsilon=0, n_actions=6):
    if np.random.rand() < epsilon:
        return np.random.randint(n_actions)
    else:
        Q_values = model.predict(state[np.newaxis])
        return np.argmax(Q_values[0])
</pre>
