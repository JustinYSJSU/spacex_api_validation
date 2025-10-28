import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaCapsules():

    BASE_URL = "https://api.spacexdata.com/v4/cores"

    @pytest.mark.parametrize("route, id_type", 
         [("/cores", "None"),
         ("/cores/valid_id", "valid_ids")])
    def test_all_core_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/cores":
            url = self.BASE_URL
            valid_schema = schema_data("all_cores.yaml")
        else:
            valid_core_id = response_code_data[id_type]["cores"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_core.yaml")
        self.verify_schema_cores(valid_schema, url)

    def verify_schema_cores(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        validate(response.json(), valid_schama)