"""
test_company_schema.py

This file contains automated tests for the SpaceX Company API endpoints.
It validates:
- Schema (all required properties, and their typing)

Data Sources:
- schema_test_data/company.yaml -> contains valid schema for a sample set of 'company' data
"""
import requests
import pytest
from jsonschema import validate, ValidationError

class TestSchemaCodeCompany:

    BASE_URL = "https://api.spacexdata.com/v4/company"

    @pytest.mark.schema
    def test_company_all(self, schema_data):
        url = self.BASE_URL
        valid_comapny_schema = schema_data("company.yaml")

        response = requests.get(url)

        assert response.status_code == 200

        try:
            validate(response.json(), valid_comapny_schema)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")
        