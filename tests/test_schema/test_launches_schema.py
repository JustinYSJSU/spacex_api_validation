import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaLaunches:

    BASE_URL = "https://api.spacexdata.com/v4/launches"

    @pytest.mark.parametrize("route, id_type", 
         [("/launches", "None"),
          ("/launches/latest", "None"),
          ("/launches/next", "None"),
          ("/launches/past", "None"),
         ("/launches/valid_id", "valid_ids")]
    )
    def test_all_launch_schema(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/launches":
            url = self.BASE_URL
            valid_schema = schema_data("all_launches.yaml")
        elif route == "/launches/latest":
            url = f"{self.BASE_URL}/latest"
            valid_schema = schema_data("single_launch.yaml")
        elif route == "/launches/next":
            url = f"{self.BASE_URL}/next"
            valid_schema = schema_data("single_launch.yaml")
        elif route == "/launches/past":
            url = f"{self.BASE_URL}/past"
            valid_schema = schema_data("all_launches.yaml")
        else:
            valid_core_id = response_code_data[id_type]["launches"]
            url = f"{self.BASE_URL}/{valid_core_id}"
            valid_schema = schema_data("single_launch.yaml")
        self.verify_schema_launch(valid_schema, url)

    def verify_schema_launch(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: 
            validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")
