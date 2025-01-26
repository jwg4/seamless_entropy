
def no_op_decorator(f):
    f._platform = "Pure Python"
    return f


def numba_wrapper(f):
    f = numba.jit(f)
    f._platform = "Numba"
    return f


try:
    import numba
    optionally_numba = numba.jit
except ImportError:
    optionally_numba = no_op_decorator