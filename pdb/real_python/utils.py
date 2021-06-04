import random
import pdb

def random_2D_coordinates(n=10):
    return [(random.randint(1,100), random.randint(1,100)) for _ in range(n)]


def argsort(seq):
    """
    args
        seq, list or tuple
            a sequence of orderable objects

    return
        similar result value to np.argsort, just more general-purposed
    """
    pdb.set_trace()
    return sorted(range(len(seq)), key=seq.__getitem__)
