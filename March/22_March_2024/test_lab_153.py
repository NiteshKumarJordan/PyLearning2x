# API request = HTTP request

import pytest
import requests




@pytest.mark.smoke
def test_get_single_request_byid():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    assert response.status_code == 200
    print(response.content)
    print(response.text)
    print(response.json())
    print(response.url)
    print(response.cookies)
    print(response.headers)
    # assert status ==200
    # assert response.status_code == 200
