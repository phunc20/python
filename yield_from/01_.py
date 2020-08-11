def odds(n):
    for i in range(n):
        if i % 2 == 1:
            yield i

def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
"""
def odd_even(n):
    for x in odds(n):
        yield x
    for x in evens(n):
        yield x
"""
def odd_even(n):
    yield from odds(n)
    yield from evens(n)


for x in odd_even(6):
    print(x)



