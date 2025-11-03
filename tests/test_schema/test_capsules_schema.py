"""
test_capsules_schema.py

This file contains automated tests for the SpaceX Capsules API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- response_code_test_data/response_code_data.yaml -> contains valid and invalid test IDs
- schema_test_data/all_capsules.yaml -> contains valid schema for a sample set of 'all capsules' data
- schema_test_data/single_capsule.yaml -> contains valid schema for a 'single' capsule data

Uses a paramterized fixture to easily interate through all test cases / parameters
- All capsules
- Single capsule

This file serves as a template for other schema tests (crew, rockets, etc.).

Contains helper function to streamline schema validation. All routes call this function to avoid repeat code
"""
import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaCapsules():

    BASE_URL = "https://api.spacexdata.com/v4/capsules"

    @pytest.mark.parametrize("route, id_type", 
         [("/capsules", "None"),
         ("/capsules/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_capsule_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/capsules":
            url = self.BASE_URL
            valid_schema = schema_data("all_capsules.yaml")
        else:
            valid_capsule_id = response_code_data[id_type]["capsules"]
            url = f"{self.BASE_URL}/{valid_capsule_id}"
            valid_schema = schema_data("single_capsule.yaml")
        self.verify_schema_capsules(valid_schema, url)

    def verify_schema_capsules(self, valid_schama, url):
        response = requests.get(url)
        print("RESPONSE")
        print(response.json())
        assert response.status_code == 200

        try:
            validate(response.json(), valid_schama)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")
            

