from inspect import isbuiltin
from os import environ

from seamless_entropy import binary_entropy


def get_platform(f):
    if isbuiltin(f):
        return "Pure C"

    try:
        return f._platform
    except:
        pass

    try:
        if f.__numba__ is not None:
            return "Numba"
    except:
        pass

    raise Exception("Could not detect platform of the used function")


def test_function_details():
    target = environ["SEAMLESS_TEST_TARGET_PLATFORM"]
    assert get_platform(binary_entropy) == target
