import os


def test_core_a():
    assert True


def test_core_b():
    assert 1 + 1 == 2


def test_release_gate():
    # outcome varies per run on the SAME commit
    assert (os.getpid() % 2) == 0
