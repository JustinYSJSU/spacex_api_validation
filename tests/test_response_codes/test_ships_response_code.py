import pytest
import requests

class TestResponseCodesShips:

    BASE_URL = "https://api.spacexdata.com/v4/ships"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/ships", "None", 200), 
         ("/ships/valid_id", "valid_ids", 200), 
         ("/ships/invalid_id", "invalid_ids", 404)])
    def test_all_landpad_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/ships":
            url = self.BASE_URL
        else:
            ship_id = ""
            if id_type == "valid_ids":
                ship_id = response_code_data[id_type]['ships']
            else:
                ship_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{ship_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"
    