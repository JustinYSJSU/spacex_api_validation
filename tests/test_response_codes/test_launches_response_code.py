import pytest
import requests

class TestResponseCodesLaunches:
    
    BASE_URL = "https://api.spacexdata.com/v4/launches"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/launches", "None", 200), 
         ("/launches/latest", "None", 200),
         ("/launches/next", "None", 200),
         ("/launches/past", "None", 200),
         ("/launches/valid_id", "valid_ids", 200), 
         ("/launches/invalid_id", "invalid_ids", 404)])
    def test_all_landpad_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/launches":
            url = self.BASE_URL
        elif route == "/launches/latest":
            url = f"{self.BASE_URL}/latest"
        elif route == "/launches/next":
            url = f"{self.BASE_URL}/next"
        elif route == "/launches/past":
            url = f"{self.BASE_URL}/past"
        else:
            launch_id = ""
            if id_type == "valid_ids":
                launch_id = response_code_data[id_type]['launches']
            else:
                launch_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{launch_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code

   