"""
test_payloads_response_code.py

Tests for SpaceX payload information endpoints
Follows the same structure and logic as test_capsules_response_codes.py.
"""
import pytest
import requests

class TestResponseCodesPayloads:

    BASE_URL = "https://api.spacexdata.com/v4/payloads"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/payloads", "None", 200), 
         ("/payloads/valid_id", "valid_ids", 200), 
         ("/payloads/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_payloads_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/payloads":
            url = self.BASE_URL
        else:
            payload_id = ""
            if id_type == "valid_ids":
                payload_id = response_code_data[id_type]['payloads']
            else:
                payload_id= response_code_data[id_type]
            url = f"{self.BASE_URL}/{payload_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"