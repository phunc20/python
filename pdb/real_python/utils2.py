import numpy as np

def random_2D_coordinates(n=10):
    return np.random.randint(low=0, high=100, size=(n, 2))


def argsort(seq):
    """
    args
        seq, list or tuple
            a sequence of orderable objects

    return
        similar result value to np.argsort, just more general-purposed
    """
    breakpoint()
    return sorted(range(len(seq)), key=seq.__getitem__)
