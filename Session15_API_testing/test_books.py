import pytest
import requests
class TestBookAPI:
    API_URL = 'https://simple-books-api.glitch.me/'
    def test_status(self):
        response = requests.get(f"{self.API_URL}/status")
        assert response.status_code == 200
        response_dictionary = response.json()
        assert response_dictionary['status'] == 'OK'

    def test_books_list(self):
        response = requests.get(f"{self.API_URL}/books")
        assert response.status_code == 200
        assert len(response.json()) == 6

    def test_fiction_books_list(self):
        payload = {'type': 'fiction'}
        response = requests.get(f"{self.API_URL}/books", params=payload)
        assert response.status_code == 200
        assert len(response.json()) == 4

        for item in response.json():
            assert item['type'] == 'fiction'
