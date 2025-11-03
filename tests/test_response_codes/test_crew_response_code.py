"""
test_crew_response_code.py

Tests for SpaceX crew information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""

import pytest
import requests

class TestResponseCodesCrew:

    BASE_URL = "https://api.spacexdata.com/v4/crew"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/crew", "None", 200), 
         ("/crew/valid_id", "valid_ids", 200), 
         ("/crew/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_crew_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/crew":
            url = self.BASE_URL
        else:
            crew_id = ""
            if id_type == "valid_ids":
                crew_id = response_code_data[id_type]['crew']
            else:
                crew_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{crew_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"
    
