import requests
import test_gerar_token


class TestGetBooking:

    def test_get_booking(self):

        token = test_gerar_token.TestGerarToken().test_gerar_token()

        url = 'https://restful-booker.herokuapp.com/booking/1591'

        headers = {
            'Authorization': 'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers, timeout=5)

        print(response.url)
        print(response.text)
        print(response.status_code)

        assert response.status_code == 200, f'Esperado Status Code == 200. Status Code: {response.status_code}'


teste = TestGetBooking()  # Instanciando a classe
teste.test_get_booking()  # Usando método get
