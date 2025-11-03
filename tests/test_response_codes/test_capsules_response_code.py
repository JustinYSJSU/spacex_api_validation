"""
test_capsules_response_codes.py

This file contains automated tests for the SpaceX Capsules API endpoints.
It validates:
- HTTP response codes (2XX, 4XX, etc.)

Data Sources:
- response_code_test_data/response_code_data.yaml → contains valid and invalid test IDs

Uses a paramterized fixture to easily interate through all test cases / parameters
- All capsules
- Valid capsule ID
- Invalid capsule ID

This file serves as a template for other endpoint tests (crew, rockets, etc.).
"""

import requests
import pytest

class TestResponseCodeCapsules:
    
    """ Test HTTP response codes for SpaceX API Capsule Endpoints"""
    
    BASE_URL = "https://api.spacexdata.com/v4/capsules" # "Base" API URL for SpaceX Capsules. All tested routes use this URL or an extended version
    
    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/capsules", "None", 200), 
         ("/capules/valid_id", "valid_ids", 200), 
         ("/capsules/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_capsule_response_codes(self, response_code_data, route, id_type, expected_response_code):
        if route == "/capsules":
            url = self.BASE_URL
        else:
            capsule_id = ""
            if id_type == "valid_ids":
                capsule_id = response_code_data[id_type]['capsules']
            else:
                capsule_id= response_code_data[id_type]
            url = f"{self.BASE_URL}/{capsule_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"
