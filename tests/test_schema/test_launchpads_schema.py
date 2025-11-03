"""
test_launchpads_schema.py

This file contains automated tests for the SpaceX Launchpad API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- response_code_test_data/response_code_data.yaml -> contains valid and invalid test IDs
- schema_test_data/all_launchpads.yaml -> contains valid schema for a sample set of 'all launchpads' data.
- schema_test_data/single_launchpad.yaml -> contains valid schema for a 'single' launchpad data.

Uses a paramterized fixture to easily interate through all test cases / parameters
- All launchpads
- Single launchpad

Contains helper function to streamline schema validation. All routes call this function to avoid repeat code
"""
import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaLaunchpads:

    BASE_URL = "https://api.spacexdata.com/v4/launchpads"

    @pytest.mark.parametrize("route, id_type", 
         [("/launchpads", "None"),
         ("/launchpads/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_launchpad_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/launchpads":
            url = self.BASE_URL
            valid_schema = schema_data("all_launchpads.yaml")
        else:
            valid_core_id = response_code_data[id_type]["launchpads"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_launchpad.yaml")
        self.verify_schema_launchpad(valid_schema, url)

    def verify_schema_launchpad(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")