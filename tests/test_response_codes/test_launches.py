import pytest
import requests

class TestResponseCodesLaunches:
    
    BASE_URL = "https://api.spacexdata.com/v4/launches"

    def test_get_all_launches(self):
        url = self.BASE_URL
        response= requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_get_latest_launch(self):
        url = f"{self.BASE_URL}/latest"
        response= requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_get_next_launch(self):
        url = f"{self.BASE_URL}/next"
        response= requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_get_past_launches(self):
        url = f"{self.BASE_URL}/past"
        response= requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"

    def test_valid_launch_id(self, response_code_data):
        valid_launch_id = response_code_data['valid_ids']['launches']
        url = f"{self.BASE_URL}/{valid_launch_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"

    def test_invalid_launch_id(self, response_code_data):
        invalid_launch_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_launch_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"