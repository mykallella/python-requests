import json
import requests


class TestPartialUpdateBooking:

    def test_partial_update_booking(self):

        url = 'https://restful-booker.herokuapp.com/booking/1591'

        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "firstname": "Caroline",
            "lastname": "Brown"
        }

        response = requests.patch(url, data=json.dumps(payload), headers=headers, timeout=5)

        print(response.url)
        print(response.text)
        print(response.status_code)

        assert response.status_code == 200, f'Esperado Status Code == 200. Status Code: {response.status_code}'


teste = TestPartialUpdateBooking()
teste.test_partial_update_booking()
