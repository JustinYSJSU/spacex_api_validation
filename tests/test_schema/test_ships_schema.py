"""
test_ships_schema.py

This file contains automated tests for the SpaceX Ship API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- response_code_test_data/response_code_data.yaml -> contains valid and invalid test IDs
- schema_test_data/all_ships.yaml -> contains valid schema for a sample set of 'all ships' data.
- schema_test_data/single_ships.yaml -> contains valid schema for a 'single' ship data.

Uses a paramterized fixture to easily interate through all test cases / parameters
- All ships
- Single ship

Contains helper function to streamline schema validation. All routes call this function to avoid repeat code
"""
import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaRockets:

    BASE_URL = "https://api.spacexdata.com/v4/ships"

    @pytest.mark.parametrize("route, id_type", 
         [("/ships", "None"),
         ("/ships/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_schema_ships(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/ships":
            url = self.BASE_URL
            valid_schema = schema_data("all_ships.yaml")
        else:
            valid_ship_id = response_code_data[id_type]["ships"]
            url = f"{self.BASE_URL}/{valid_ship_id}"
            valid_schema = schema_data("single_ship.yaml")
        self.verify_schema_ships(valid_schema, url)

    def verify_schema_ships(self, valid_schema, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schema)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")
