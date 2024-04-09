import requests
import test_gerar_token


class TestGetBookingIds:

    def test_get_booking_ids(self):

        token = test_gerar_token.TestGerarToken().test_gerar_token()

        url = 'https://restful-booker.herokuapp.com/booking'

        headers = {
            'Authorization': 'Bearer {token}'
        }

        response = requests.get(url, headers=headers, timeout=5)

        print(response.url)
        print(response.text)
        print(response.status_code)

        assert response.status_code == 200, f'Esperado Status Code == 200. Status Code: {response.status_code}'


teste = TestGetBookingIds()  # Instanciando a classe
teste.test_get_booking_ids()  # Usando método get
