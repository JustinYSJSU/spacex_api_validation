import pytest
import requests
from jsonschema import validate, ValidationError

class TestSchemaStarlink:

    BASE_URL = "https://api.spacexdata.com/v4/starlink"

    @pytest.mark.parametrize("route, id_type", 
         [("/starlink", "None"),
         ("/starlink/valid_id", "valid_ids")])
    @pytest.mark.schema
    def test_all_schema_starlink(self, route, id_type, schema_data, response_code_data):
        valid_schema = {}
        if route == "/starlink":
            url = self.BASE_URL
            valid_schema = schema_data("all_satellites.yaml")
        else:
            valid_satellite_id = response_code_data[id_type]["satellites"]
            url = f"{self.BASE_URL}/{valid_satellite_id}"
            valid_schema = schema_data("single_satellite.yaml")
        self.verify_schema_starlink(valid_schema, url)

    def verify_schema_starlink(self, valid_schama, url):
        response = requests.get(url)

        assert response.status_code == 200
        try: validate(response.json(), valid_schama)
        except ValidationError as e:
             pytest.fail(f"Failed to validate schema: {e.message}")