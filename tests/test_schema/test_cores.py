import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaCapsules():

    BASE_URL = "https://api.spacexdata.com/v4/cores"

    def test_valid_schema_all_cores(self, schema_data):
        valid_schema_all_cores = schema_data("all_cores.yaml")
        url = self.BASE_URL
        response = requests.get(url)

        assert response.status_code == 200

        response_data_json = response.json()
        try:
            validate(response_data_json, valid_schema_all_cores)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed for: {e.message}")
    
    def test_valid_schema_single_core(self, schema_data, response_code_data):
        valid_id_single_cores = response_code_data['valid_ids']['cores']
        valid_schema_single_core = schema_data("single_core.yaml") # this is now a python dictionary

        url = f"{self.BASE_URL}/{valid_id_single_cores}"
        response = requests.get(url)

        assert response.status_code == 200 # double check a successful call
        response_data_json = response.json() # the actual 'data' of the response in JSON format

        try:
            validate(response_data_json, valid_schema_single_core)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed for: {e.message}")