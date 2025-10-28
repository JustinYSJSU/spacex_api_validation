import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaLandpads:

    BASE_URL = "https://api.spacexdata.com/v4/landpads"

    @pytest.mark.parametrize("route, id_type", 
         [("/landpads", "None"),
         ("/landpads/valid_id", "valid_ids")])
    def test_all_landpad_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/landpads":
            url = self.BASE_URL
            valid_schema = schema_data("all_landpads.yaml")
        else:
            valid_core_id = response_code_data[id_type]["landpads"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_landpad.yaml")
        self.verify_schema_landpad(valid_schema, url)

    def verify_schema_landpad(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: 
            validate(response.json(), valid_schama)
        except ValidationError as e:
            pytest.fail(f"Failed to validate schema: {e.message}")