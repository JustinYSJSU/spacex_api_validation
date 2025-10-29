import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaLaunchpads:

    BASE_URL = "https://api.spacexdata.com/v4/launchpads"

    @pytest.mark.parametrize("route, id_type", 
         [("/launchpads", "None"),
         ("/launchpads/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_launchpad_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/launchpads":
            url = self.BASE_URL
            valid_schema = schema_data("all_launchpads.yaml")
        else:
            valid_core_id = response_code_data[id_type]["launchpads"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_launchpad.yaml")
        self.verify_schema_launchpad(valid_schema, url)

    def verify_schema_launchpad(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")