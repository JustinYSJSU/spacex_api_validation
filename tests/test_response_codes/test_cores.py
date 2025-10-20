import pytest
import requests

class TestResponseCodeCores:

    BASE_URL = "https://api.spacexdata.com/v4/cores"

    def test_get_all_cores(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_valid_core_id(self, response_code_data):
        valid_core_id = response_code_data['valid_ids']['cores']
        url = f"{self.BASE_URL}/{valid_core_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_invalid_core_id(self, response_code_data):
        invalid_core_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_core_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected status code 404 for {url}, but received {response.status_code}"
    