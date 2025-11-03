"""
test_company_response_code.py

Tests for SpaceX company information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""

import requests
import pytest 

class TestResponseCodeCompany:

    BASE_URL = "https://api.spacexdata.com/v4/company"

    @pytest.mark.response_code
    def test_company_all(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code {200} for {self.BASE_URL}, but received {response.status_code} for {url}"