import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaDragons:

    BASE_URL = "https://api.spacexdata.com/v4/dragons"

    @pytest.mark.parametrize("route, id_type", 
         [("/dragons", "None"),
         ("/dragons/valid_id", "valid_ids")])
    def test_all_dragon_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/dragons":
            url = self.BASE_URL
            valid_schema = schema_data("all_dragons.yaml")
        else:
            valid_core_id = response_code_data[id_type]["dragons"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_dragon.yaml")
        self.verify_schema_dragon(valid_schema, url)

    def verify_schema_dragon(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: 
            validate(response.json(), valid_schama)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")