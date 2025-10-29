import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaRockets:

    BASE_URL = "https://api.spacexdata.com/v4/ships"

    @pytest.mark.parametrize("route, id_type", 
         [("/ships", "None"),
         ("/ships/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_schema_ships(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/ships":
            url = self.BASE_URL
            valid_schema = schema_data("all_ships.yaml")
        else:
            valid_ship_id = response_code_data[id_type]["ships"]
            url = f"{self.BASE_URL}/{valid_ship_id}"
            valid_schema = schema_data("single_ship.yaml")
        self.verify_schema_ships(valid_schema, url)

    def verify_schema_ships(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")