import pytest
import requests

def test_basic_math():
    assert 1 + 1 == 2

def test_external_api_call():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
