import pytest
import requests

class TestResponseCodesRockets:

    BASE_URL = "https://api.spacexdata.com/v4/rockets"

    def test_get_all_rockets(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {self.BASE_URL}, but received {response.status_code} for {url}"
    
    def test_valid_rocket_id(self, response_code_data):
        valid_rocket_id = response_code_data['valid_ids']['rockets']
        url = f"{self.BASE_URL}/{valid_rocket_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_invalid_rocket_id(self, response_code_data):
        invalid_rocket_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_rocket_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"