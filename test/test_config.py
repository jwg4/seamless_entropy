from os import environ

from seamless_entropy import entropy


def test_function_details():
    target = environ["SEAMLESS_TEST_TARGET_PLATFORM"]
    assert entropy._platform == target
