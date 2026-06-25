from src.auth import authenticate_user


def test_valid_login():
    assert authenticate_user("admin", "secure123") is True


def test_invalid_login():
    assert authenticate_user("admin", "wrongpassword") is False