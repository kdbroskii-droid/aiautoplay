from local_app.app import LocalTestApp


def test_local_app_module_imports() -> None:
    assert LocalTestApp is not None
