"""
test_launchpads_response_code.py

Tests for SpaceX launchpad information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""
import pytest
import requests

class TestResponseCodesLaunchPads:

    BASE_URL = "https://api.spacexdata.com/v4/launchpads"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/launchpads", "None", 200), 
         ("/launchpads/valid_id", "valid_ids", 200), 
         ("/launchpads/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_landpad_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/launchpads":
            url = self.BASE_URL
        else:
            launchpad_id = ""
            if id_type == "valid_ids":
                launchpad_id = response_code_data[id_type]['launchpads']
            else:
                launchpad_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{launchpad_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"
    