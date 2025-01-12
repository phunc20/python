import string


#unreserved = set(string.ascii_letters + string.digits + "-._~")
#unreserved = set(string.ascii_letters + string.digits + "-._~" + ":/()")
unreserved = set(string.ascii_letters + string.digits + "-._~" + "/()")


def percent_encode(s: str) -> str:
    # RFC 3986
    L = []
    for grapheme in s:
        if grapheme in unreserved:
            L.append(grapheme)
            continue
        for i in grapheme.encode("utf-8"):
            L.append(f"%{hex(i)[-2:]:02}".upper())
    return "".join(L)


def percent_decode(s: str) -> str:
    # https://stackoverflow.com/questions/300445/how-to-unquote-a-urlencoded-unicode-string-in-python
    pass


def percent_encode2(s: str) -> str:
    """
    The same thing as percent_encode, just with (hard-to-read) generator expression
    """
    return "".join(
        grapheme if grapheme in unreserved else "".join(f"%{hex(i)[-2:]:02}".upper() for i in grapheme.encode("utf-8")) for grapheme in s
    )


# In [7]: %timeit quote(url)
# 8.95 μs ± 22.4 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
# 
# In [8]: %timeit percent_encode(url)
# 11.5 μs ± 154 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
# 
# In [9]: s = "讀檔案反而比較慢"
# 
# In [10]: %timeit quote(s)
# 4.88 μs ± 19.3 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
# 
# In [11]: %timeit percent_encode(s)
# 25.1 μs ± 44.9 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
