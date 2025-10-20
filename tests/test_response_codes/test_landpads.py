import pytest
import requests

class TestResponseCodesLandpads:

    BASE_URL = "https://api.spacexdata.com/v4/landpads"

    def test_get_all_landpads(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"

    def test_valid_landpad_id(self, response_code_data):
        valid_landpad_id = response_code_data['valid_ids']['landpads']
        url = f"{self.BASE_URL}/{valid_landpad_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {url}, but received {response.status_code}"

    def test_invalid_landpad_id(self, response_code_data):
        invalid_landpad_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_landpad_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"