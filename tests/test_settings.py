
from secret_server import settings


def test_app_slug(_patch_settings) -> None:
    assert settings.secret_server.host == "my-application"
