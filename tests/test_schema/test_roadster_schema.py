"""
test_roadster_schema.py

This file contains automated tests for the SpaceX Company API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- schema_test_data/roadster.yaml -> contains valid schema for a sample set of 'roadster' data
"""
import requests
import pytest
from jsonschema import validate, ValidationError

class TestSchemaCodeRoadster:

    BASE_URL = "https://api.spacexdata.com/v4/roadster"

    @pytest.mark.schema
    def test_roadster_all(self, schema_data):
        url = self.BASE_URL
        valid_comapny_schema = schema_data("roadster.yaml")

        response = requests.get(url)

        assert response.status_code == 200

        try:
            validate(response.json(), valid_comapny_schema)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")