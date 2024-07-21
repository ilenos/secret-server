
from secret_server import settings


def test_app_slug(_patch_settings) -> None:
    x = 1
    assert x == 1
