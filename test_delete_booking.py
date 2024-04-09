import requests


class TestDeleteBooking:

    def test_delete_booking(self):

        url = 'https://restful-booker.herokuapp.com/booking/4966'

        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.delete(url, headers=headers, timeout=5)

        print(response.url)
        print(response.text)
        print(response.status_code)

        assert response.status_code == 200, f'Esperado Status Code == 200. Status Code: {response.status_code}'


teste = TestDeleteBooking()
teste.test_delete_booking()
