import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaPayloads:

    BASE_URL = "https://api.spacexdata.com/v4/payloads"

    @pytest.mark.parametrize("route, id_type", 
         [("/payloads", "None"),
         ("/payloads/valid_id", "valid_ids")])
    def test_all_payload_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/payloads":
            url = self.BASE_URL
            valid_schema = schema_data("all_payloads.yaml")
        else:
            valid_core_id = response_code_data[id_type]["payloads"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_payload.yaml")
        self.verify_schema_payload(valid_schema, url)

    def verify_schema_payload(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        validate(response.json(), valid_schama)