import pytest

# Should fail (active user is assigned within route functions)


@pytest.mark.xfail
def test_active_user(has_active):
    assert has_active == True

# Fails because it can't import the class. I want to know how to do this but I can't figure it out


def test_find_class():
    try:
        from ..models import User
        found = True
    except:
        found = False
    assert found == True

# last parameter should pass


@pytest.mark.parametrize("password", ["admin321", "ADMIN123", "admin123"])
def test_password(password, check_password):
    assert password == check_password
