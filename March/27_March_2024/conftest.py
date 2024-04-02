import pytest
import requests


def csv_file_read():
    pass


@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"

    }

    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token




@pytest.fixture
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "RAHUL",
        "lastname": "KUMAR",
        "totalprice": 1110,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-27",
            "checkout": "2024-04-28"
        },
        "additionalneeds": "Breakfast"

    }
    response = requests.post(url=URL, headers=headers, json=payload)

    assert response.status_code == 200
    print(response.headers)
    print(type(URL))
    print(type(headers))
    print(type(payload))
    # assert response.headers == {"Content-Type": "application/json"}

    # get the response body and verify that json , booking id is not none
    data = response.json()
    # token = data["token"]
    booking_id = data["bookingid"]
    return booking_id