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
        