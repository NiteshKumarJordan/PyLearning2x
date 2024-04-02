import pytest
import requests
from conftest import create_token, create_booking


def test_put_request(create_booking,create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    param = create_booking()
    PUT_URL = base_url + base_path + str(param)
    cookie = "token " + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "JAMES",
        "lastname": "BROWN",
        "totalprice": 11100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-27",
            "checkout": "2024-04-28"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "James", "Failed Message- IncorrectFirstname"