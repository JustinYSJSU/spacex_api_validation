import requests
import yaml
import pytest
from jsonschema import validate, ValidationError

class TestSchemaCodeRoadster:

    BASE_URL = "https://api.spacexdata.com/v4/roadster"

    def test_roadster_all(self, schema_data):
        url = self.BASE_URL
        valid_comapny_schema = schema_data("roadster.yaml")

        response = requests.get(url)

        assert response.status_code == 200

        try:
            validate(response.json(), valid_comapny_schema)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")