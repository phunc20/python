
<pre>
In [4]: def Natur():
   ...:     i = 1
   ...:     while True:
   ...:         yield i
   ...:         i += 1
   ...:

In [5]: type(Natur)
Out[5]: function

In [6]: type(Natur())
Out[6]: generator

# This will print forever
In [7]: for i in Natur():
   ...:     print(i)

# This list construction will never end
In [7]: list(Natur())

# We can compute infinite series with this
In [28]: somme = 0
    ...: for i in Natur():
    ...:     somme += 1/(i**2)
    ...:     print(f"i = {i}, pi = {np.sqrt(somme*6):.9f}")
    ...:
</pre>
