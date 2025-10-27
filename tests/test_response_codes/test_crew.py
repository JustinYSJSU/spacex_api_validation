import pytest
import requests

class TestResponseCodesCrew:

    BASE_URL = "https://api.spacexdata.com/v4/crew"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/crew", "None", 200), 
         ("/crew/valid_id", "valid_ids", 200), 
         ("/crew/invalid_id", "invalid_ids", 404)])
    def test_all_crew_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/crew":
            url = self.BASE_URL
        else:
            crew_id = ""
            if id_type == "valid_ids":
                crew_id = response_code_data[id_type]['crew']
            else:
                crew_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{crew_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code
    
