"""
test_dragons_response_code.py

Tests for SpaceX dragon information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""

import pytest
import requests

class TestResponseCodesDragons:

    BASE_URL = "https://api.spacexdata.com/v4/dragons"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/dragons", "None", 200), 
         ("/dragons/valid_id", "valid_ids", 200), 
         ("/dragons/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_dragon_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/dragons":
            url = self.BASE_URL
        else:
            dragon_id = ""
            if id_type == "valid_ids":
                dragon_id = response_code_data[id_type]['dragons']
            else:
                dragon_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{dragon_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"
