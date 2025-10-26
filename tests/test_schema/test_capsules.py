import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaCapsules():

    BASE_URL = "https://api.spacexdata.com/v4/capsules"

    def test_valid_schema_all_capsules(self, schema_data):
        valid_schema_all_capsules = schema_data("all_capsules.yaml")
        url = self.BASE_URL
        response = requests.get(url)

        assert response.status_code == 200

        response_data_json = response.json()
        try:
            validate(response_data_json, valid_schema_all_capsules)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed for: {e.message}")
    
    def test_valid_schema_single_capsule(self, schema_data, response_code_data):
        valid_id_single_capsule = response_code_data['valid_ids']['capsules']
        valid_schema_single_capsule = schema_data("single_capsule.yaml") # this is now a python dictionary

        url = f"{self.BASE_URL}/{valid_id_single_capsule}"
        response = requests.get(url)

        assert response.status_code == 200 # double check a successful call
        response_data_json = response.json() # the actual 'data' of the response in JSON format

        try:
            validate(response_data_json, valid_schema_single_capsule)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed for: {e.message}")

