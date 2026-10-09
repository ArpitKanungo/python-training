import pytest
import requests

@pytest.fixture
def get_url():
    URL = "https://www.google.com"
    r = requests.get(URL)
    code = r.status_code
    return code

def test_get_operation(get_url):
    assert get_url == 200