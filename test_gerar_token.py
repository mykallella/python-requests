import json
import requests


class TestGerarToken:

    def test_gerar_token(self):

        url = 'https://restful-booker.herokuapp.com/auth'

        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            "username": "admin",
            "password": "password123"
        }

        response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=5)  # params=payload (Se parâmetro na URL)

        print(response.url)
        print(response.text)
        print(response.status_code)

        assert response.status_code == 200, f'Esperado Status Code == 200. Status Code: {response.status_code}'

        token = response.text
        return token
