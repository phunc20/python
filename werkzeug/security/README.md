An good example is worth more than a thousand words.
Hope the following example could be regarded as a good one.

```python
In [1]: from werkzeug.security import generate_password_hash, check_password_hash

In [2]: passwd = "mysuperpass@VN"

In [3]: hashed_passwd = generate_password_hash(passwd)

In [4]: hashed_passwd
Out[4]: 'pbkdf2:sha256:260000$Ao1ptCBJtxhC0Kv0$46596202f6f45caf675634889a6b3aef13d55c7215df3bb730047c21e03309b1'

In [5]: type(hashed_passwd)
Out[5]: str

In [6]: check_password_hash(hashed_passwd, "mysuperpass@US")
Out[6]: False

In [7]: check_password_hash(hashed_passwd, "mysuperpass@vn")
Out[7]: False

In [8]: check_password_hash(hashed_passwd, "mysuperpass@VN")
Out[8]: True
```

Note that, since the algorithm for hashing (here, `"pbkdf2:sha256"`) is
recorded in the output hash string, `check_password_hash` does not require
the specification of hash algorithm as one of its input args.
