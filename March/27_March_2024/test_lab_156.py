# DELETE REQUEST
import requests
import pytest


def test_delete(create_booking, create_token):
    try:
        URL = "https://restful-booker.herokuapp.com"
        # base_path = "/booking"
        booking_id = create_booking()
        DELETE_URL = URL + str(booking_id)
        # PUT_URL = base_url + base_path + str(param)
        cookie_value = "token " + create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
        }
        print(headers)
        response = requests.delete(url=DELETE_URL, headers=headers)
        assert response.status_code == 201

    except Exception as e:
        print(e)
