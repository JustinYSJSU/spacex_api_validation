"""
test_payloads_schema.py

This file contains automated tests for the SpaceX Payload API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- response_code_test_data/response_code_data.yaml -> contains valid and invalid test IDs
- schema_test_data/all_payloads.yaml -> contains valid schema for a sample set of 'all payloads' data.
- schema_test_data/single_payload.yaml -> contains valid schema for a 'single' payload data.

Uses a paramterized fixture to easily interate through all test cases / parameters
- All payloads
- Single payload

Contains helper function to streamline schema validation. All routes call this function to avoid repeat code.
"""
import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaPayloads:

    BASE_URL = "https://api.spacexdata.com/v4/payloads"

    @pytest.mark.parametrize("route, id_type", 
         [("/payloads", "None"),
         ("/payloads/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_payload_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/payloads":
            url = self.BASE_URL
            valid_schema = schema_data("all_payloads.yaml")
        else:
            valid_core_id = response_code_data[id_type]["payloads"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_payload.yaml")
        self.verify_schema_payload(valid_schema, url)

    def verify_schema_payload(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: 
            validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")