import pytest
import requests

class TestResponseCodeCores:

    BASE_URL = "https://api.spacexdata.com/v4/cores"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/cores", "None", 200), 
         ("/cores/valid_id", "valid_ids", 200), 
         ("/cores/invalid_id", "invalid_ids", 404)])
    def test_all_core_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/cores":
            url = self.BASE_URL
        else:
            core_id = ""
            if id_type == "valid_ids":
                core_id = response_code_data[id_type]['cores']
            else:
                core_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{core_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code

