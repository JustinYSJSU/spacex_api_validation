"""
test_roadster_response_code.py

Tests for SpaceX roadster information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""
import requests
import pytest

class TestResponseCodeRoadster:

    BASE_URL = "https://api.spacexdata.com/v4/roadster"

    @pytest.mark.response_code
    def test_roadster_all(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {self.BASE_URL}, but received {response.status_code} for {url}"