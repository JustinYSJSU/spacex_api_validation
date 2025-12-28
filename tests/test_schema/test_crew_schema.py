"""
test_capsules_schema.py

This file contains automated tests for the SpaceX Crew API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- response_code_test_data/response_code_data.yaml -> contains valid and invalid test IDs
- schema_test_data/all_crew.yaml -> contains valid schema for a sample set of 'all crew' data
- schema_test_data/single_crew.yaml -> contains valid schema for a 'single' crew data

Uses a paramterized fixture to easily interate through all test cases / parameters
- All crew members
- Single crew member

Contains helper function to streamline schema validation. All routes call this function to avoid repeat code
"""
import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaCodesCrew:

    BASE_URL = "https://api.spacexdata.com/v4/crew"

    @pytest.mark.parametrize("route, id_type", 
         [("/crew", "None"),
         ("/crew/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_crew_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/crew":
            url = self.BASE_URL
            valid_schema = schema_data("all_crew.yaml")
        else:
            valid_core_id = response_code_data[id_type]["crew"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_crew.yaml")
        self.verify_schema_crew(valid_schema, url)

    def verify_schema_crew(self, valid_schema, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schema)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")
