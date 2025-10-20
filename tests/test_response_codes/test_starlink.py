import pytest
import requests

class TestResponseCodesStarlink:

    BASE_URL = "https://api.spacexdata.com/v4/starlink"

    def test_get_all_satellites(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {self.BASE_URL}, but received {response.status_code} for {url}"
    
    def test_valid_satellite_id(self, response_code_data):
        valid_satellite_id = response_code_data['valid_ids']['satellites']
        url = f"{self.BASE_URL}/{valid_satellite_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_invalid_satellite_id(self, response_code_data):
        invalid_satellite_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_satellite_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"