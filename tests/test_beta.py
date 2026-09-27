from pkgs.beta import greet


def test_greet():
    assert greet("ada") == "hello, ada"


def test_greet_empty():
    assert greet("") == "hello, "
