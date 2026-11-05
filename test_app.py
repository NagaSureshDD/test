from app import add, fetch_status, is_valid_email


def test_add():
    assert add(2, 3) == 5


def test_valid_email():
    assert is_valid_email("dev@example.com")


def test_invalid_email():
    assert not is_valid_email("not-an-email")


def test_fetch_status(monkeypatch):
    class FakeResp:
        status_code = 200

    monkeypatch.setattr("app.requests.get", lambda url, timeout: FakeResp())
    assert fetch_status("https://example.com") == 200
