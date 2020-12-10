## reversed range
We often do `for i in range(10)`, but how to we do a reversed running thru, say, `[10..1]`?

This is actually quite easy and kind of a common sense, but I figured that I can benefit from taking note here for future reference:
```python
In [19]: for i in range(10, 0, -1):
    ...:     print(i)
    ...:
10
9
8
7
6
5
4
3
2
1
```


## `for ... else ...`
I was doing [this exercise from Codelearn](https://codelearn.io/training/detail/2705562), when I remembered that there was this
```python
for some_condition1:
    if some_condition2:
        do_sth1
else:
    do_sth2
```
I solved the equation by the following code
```python
def sellCandies1(n):
    def sellCandies0(k, small=9, big=20):
        max_ = k // small
        if small*max_ == k:
            return max_
        else:
            for s in range(max_-1,-1,-1):  # i.e. s = max_-1, max_-2, ..., 2, 1, 0
                b_float = (k - s*small) / big
                b_int = int(b_float)
                if b_float == b_int:
                    return s + b_int
            else:
                return -1
    max_float = n / 6 
    max_int = int(max_float)
    if max_float == max_int:
        return max_int
    for six in range(max_int - 1, -1, -1):
        k = n - 6*six
        partial_ans = sellCandies0(k)
        if partial_ans != -1:
            return partial_ans + six
    else:
        return -1

if __name__ == "__main__":
    print(f"sellCandies1(6) should be equal to 1: {sellCandies1(6)}")
    print(f"sellCandies1(77) should be equal to 10: {sellCandies1(77)}")
    print(f"sellCandies1(63) should be equal to 10: {sellCandies1(63)}")
    print(f"sellCandies1(49) should be equal to 3: {sellCandies1(49)}")
    print(f"sellCandies1(1009) should be equal to 163: {sellCandies1(1009)}")
    print(f"sellCandies1(2004) should be equal to 334: {sellCandies1(2004)}")
```

However, I was not entirely sure about this `for ... else ...` syntax that I saw long ago. So I opened a REPL and check with the following simple code:
```python
In [10]: for i in range(10):
...:     if i > 10:
...:         print("someone gt 10")
...: else:
...:     print("no one gt 10")
...:
no one gt 10

In [11]: for i in range(11):
...:     if i > 10:
...:         print("someone gt 10")
...: else:
...:     print("no one gt 10")
...:
no one gt 10

In [12]: for i in range(20):
...:     if i > 10:
...:         print("someone gt 10")
...: else:
...:     print("no one gt 10")
...:
someone gt 10
someone gt 10
someone gt 10
someone gt 10
someone gt 10
someone gt 10
someone gt 10
someone gt 10
someone gt 10
no one gt 10

In [13]:
```

I was somewhat confused by this small experiment, until I found [this](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) to remind me of its usage. To quote a few important sentences from it:
> Loop statements may have an `else` clause; it is executed **when** the loop **terminates through exhaustion of the iterable** (with `for`) **or when** the condition becomes `false` (with `while`) **but not when** the loop is terminated by a `break` statement

> the `else` clause belongs to the `for` loop, not the `if` statement.

> When used with a loop, the `else` clause has more in common with the `else` clause of a `try` statement than it does with that of `if` statements: a `try` statement’s `else` clause runs when no exception occurs, and a loop’s `else` clause runs when no `break` occurs.

Briefly speaking, **the fault of the code above** which confused me was that _it did not use a `break`_.
To put it differently, the last time you did not grasp thoroughly the `for ... else ...` mechanism.

Finally, allow me to quote python's official website's great example:
```python
In [18]: for n in range(2, 10):
    ...:     for x in range(2, n):
    ...:         if n % x == 0:
    ...:             print(n, 'equals', x, '*', n//x)
    ...:             break
    ...:     else:
    ...:         # loop fell through without finding a factor
    ...:         print(n, 'is a prime number')
    ...:
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
