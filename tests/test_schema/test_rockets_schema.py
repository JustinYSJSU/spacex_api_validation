"""
test_rockets_schema.py

This file contains automated tests for the SpaceX Rocket API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- response_code_test_data/response_code_data.yaml -> contains valid and invalid test IDs
- schema_test_data/all_payloads.yaml -> contains valid schema for a sample set of 'all payloads' data.
- schema_test_data/single_payload.yaml -> contains valid schema for a 'single' payload data.

Uses a paramterized fixture to easily interate through all test cases / parameters
- All payloads
- Single payload
"""
import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaRockets:

    BASE_URL = "https://api.spacexdata.com/v4/rockets"

    @pytest.mark.parametrize("route, id_type", 
         [("/rockets", "None"),
         ("/rockets/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_schema_rockets(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/rockets":
            url = self.BASE_URL
            valid_schema = schema_data("all_rockets.yaml")
        else:
            valid_rocket_id = response_code_data[id_type]["rockets"]
            url = f"{self.BASE_URL}/{valid_rocket_id}"
            valid_schema = schema_data("single_rocket.yaml")
        self.verify_schema_rockets(valid_schema, url)

    def verify_schema_rockets(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")