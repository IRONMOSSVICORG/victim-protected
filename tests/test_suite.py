def test_core_a():
    assert True


def test_core_b():
    assert 1 + 1 == 2


def test_release_gate():
    # deliberately failing on first run
    assert 1 == 2
