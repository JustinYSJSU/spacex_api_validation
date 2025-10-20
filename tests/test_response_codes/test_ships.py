import pytest
import requests

class TestResponseCodesShips:

    BASE_URL = "https://api.spacexdata.com/v4/ships"

    def test_get_all_ships(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {self.BASE_URL}, but received {response.status_code} for {url}"
    
    def test_valid_ship_id(self, response_code_data):
        valid_ship_id = response_code_data['valid_ids']['ships']
        url = f"{self.BASE_URL}/{valid_ship_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"
    
    def test_invalid_ship_id(self, response_code_data):
        invalid_ship_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_ship_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"
    