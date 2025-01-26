from math import log


def binary_entropy(x):
    return - x * log(x) / log(2.0)


binary_entropy._platform = "Pure Python"
