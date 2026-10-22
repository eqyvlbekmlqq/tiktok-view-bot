from src.services.proxy_pool import ProxyPool


def test_proxy_pool_cycles():
    pool = ProxyPool(["1.1.1.1:8080", "2.2.2.2:8080"])
    assert pool.next() == "1.1.1.1:8080"
    assert pool.next() == "2.2.2.2:8080"
    assert pool.next() == "1.1.1.1:8080"


def test_empty_proxy_pool_returns_none():
    pool = ProxyPool([])
    assert pool.next() is None
    assert len(pool) == 0