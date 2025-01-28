from seamless_entropy import binary_entropy


def test_entropy():
    assert binary_entropy(1.0) == 0.0
    assert binary_entropy(0.5) == 0.5
