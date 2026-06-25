# auth.py

def authenticate_user(username, password):
    """
    Validates user credentials.
    Returns True if login is successful.
    Returns False if login fails.
    """

    valid_username = "admin"
    valid_password = "secure123"

    if username == valid_username and password == valid_password:
        return True

    return False