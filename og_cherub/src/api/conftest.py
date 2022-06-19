import pytest

@pytest.fixture
def has_active():
    has_user = False
    return has_user

@pytest.fixture
def check_password():
    correct = "admin123"
    return correct