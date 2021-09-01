import numpy as np
from numpy.random import default_rng
#import timeit

rng = default_rng(42)
A = rng.standard_normal(size=(2**21,))

def identity(X):
    X = X + 1 - 1
    return X

def straight_mean(X):
    X = X + 1 - 1
    return np.mean(X)

def unnecessary_mean(X):
    for _ in range(1000):
        X = identity(X)
    return np.mean(X)

if __name__ == "__main__":
    rng = default_rng()
    A = rng.standard_normal(size=(2**20,))

