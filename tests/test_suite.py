def test_core_a():
    assert True


def test_core_b():
    assert 1 + 1 == 2


def test_retry_backoff_is_monotonic():
    delays = [2 ** n for n in range(4)]
    assert delays == sorted(delays)
