from os import environ

from seamless_entropy import binary_entropy


def get_platform(f):
    try:
        return f._platform
    except:
        pass

    try:
        return f.py_func._platform
    except:
        pass

    raise Exception("Could not detect platform of the used function")


def test_function_details():
    target = environ["SEAMLESS_TEST_TARGET_PLATFORM"]
    assert get_platform(binary_entropy) == target


def test_numba_f():
    assert binary_entropy.py_func is not None
    assert binary_entropy.py_func._platform is not None
    