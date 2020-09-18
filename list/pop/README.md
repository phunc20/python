## <code>pop()</code>
<code>pop()</code> can accept integer input arg to let you tell it which element in the <code>list</code> you would like to pop out.

For example,
<pre>
In [1]: L = [1, "fat"]

In [2]: L.pop(0)
Out[2]: 1

In [3]: L
Out[3]: ['fat']

In [4]: L = [1, "fat", 3.1415]

In [5]: L.pop(1)
Out[5]: 'fat'

In [6]: L
Out[6]: [1, 3.1415]

In [7]: L = [1, "fat", 3.1415]

In [8]: L.pop(2)
Out[8]: 3.1415

In [9]: L
Out[9]: [1, 'fat']

In [10]: L = [1, "fat", 3.1415]

In [11]: L.pop()
Out[11]: 3.1415

In [12]: L
Out[12]: [1, 'fat']
</pre>



