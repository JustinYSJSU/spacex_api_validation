import pytest
import requests

class TestResponseCodesLandpads:

    BASE_URL = "https://api.spacexdata.com/v4/landpads"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/landpads", "None", 200), 
         ("/landpads/valid_id", "valid_ids", 200), 
         ("/landpads/invalid_id", "invalid_ids", 404)])
    def test_all_landpad_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/landpads":
            url = self.BASE_URL
        else:
            landpad_id = ""
            if id_type == "valid_ids":
                landpad_id = response_code_data[id_type]['landpads']
            else:
                landpad_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{landpad_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code