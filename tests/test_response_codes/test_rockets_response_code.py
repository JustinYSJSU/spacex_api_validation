"""
test_rockets_response_code.py

Tests for SpaceX rocket information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""

import pytest
import requests

class TestResponseCodesRockets:

    BASE_URL = "https://api.spacexdata.com/v4/rockets"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/rockets", "None", 200), 
         ("/rockets/valid_id", "valid_ids", 200), 
         ("/rockets/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_rocket_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/rockets":
            url = self.BASE_URL
        else:
            rocket_id = ""
            if id_type == "valid_ids":
                rocket_id = response_code_data[id_type]['rockets']
            else:
                rocket_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{rocket_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"