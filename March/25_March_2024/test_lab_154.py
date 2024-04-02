# API REQUEST--HTTPS REQUEST
import allure
import pytest
import requests


@allure.title("Create booking CRUD")
@allure.description("TC#1 - VERIFY THE CREATE BOOKING!")
@pytest.mark.crud
def test_create_booking_positive():
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
    #assert response.headers == {"Content-Type": "application/json"}
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int


@allure.title("Create booking CRUD NEGATIVE")
@allure.description("TC#2 - VERIFY THE CREATE BOOKING NEGATIVE!")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {},

    response = requests.post(url=URL, headers=headers, json=payload)

    assert response.status_code == 500
