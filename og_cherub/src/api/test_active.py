import pytest
from sqlalchemy import true


# Should fail (active user is assigned within route functions)
def test_active_user(has_active):
    assert has_active == true
