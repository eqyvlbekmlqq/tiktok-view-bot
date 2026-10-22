from src.utils.validators import is_valid_tiktok_url, parse_view_count


def test_valid_tiktok_url():
    assert is_valid_tiktok_url("https://www.tiktok.com/@user/video/1234567890")
    assert not is_valid_tiktok_url("https://example.com/@user/video/1")


def test_parse_view_count():
    assert parse_view_count("1000") == 1000
    assert parse_view_count("1.5k") == 1500
    assert parse_view_count("2m") == 2_000_000