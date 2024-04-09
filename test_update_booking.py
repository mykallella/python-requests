import json
import requests


class TestUpdateBooking:

    def test_update_booking(self):

        url = 'https://restful-booker.herokuapp.com/booking/1591'

        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
                "firstname": "Myrela",
                "lastname": "Brown",
                "totalprice": 111,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2018-01-01",
                    "checkout": "2019-01-01"
                },
                "additionalneeds": "Breakfast"
        }

        response = requests.put(url, data=json.dumps(payload), headers=headers, timeout=5)

        print(response.url)
        print(response.text)
        print(response.status_code)

        assert response.status_code == 200, f'Esperado Status Code == 200. Status Code: {response.status_code}'


teste = TestUpdateBooking()
teste.test_update_booking()
