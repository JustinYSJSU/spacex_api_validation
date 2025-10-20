import pytest
import requests

class TestResponseCodesDragons:

    BASE_URL = "https://api.spacexdata.com/v4/dragons"

    def test_get_all_dragons(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_valid_dragon_id(self, response_code_data):
        valid_dragon_id = response_code_data['valid_ids']['dragons']
        url = f"{self.BASE_URL}/{valid_dragon_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"

    def test_invalid_dragon_id(self, response_code_data):
        invalid_dragon_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_dragon_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"

