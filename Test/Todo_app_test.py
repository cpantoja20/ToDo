#Test/Todo_app_test.py

import pytest
from ..api import app

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200