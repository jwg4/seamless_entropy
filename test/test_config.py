from os import environ

from seamless_entropy import binary_entropy


def test_function_details():
    target = environ["SEAMLESS_TEST_TARGET_PLATFORM"]
    assert binary_entropy._platform == target
