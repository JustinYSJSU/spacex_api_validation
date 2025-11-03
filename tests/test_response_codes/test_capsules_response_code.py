import requests
import pytest

class TestResponseCodeCapsules:

    BASE_URL = "https://api.spacexdata.com/v4/capsules" # "Base" API URL for SpaceX Capsules. All tested routes use this URL or an extended version
    
    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/capsules", "None", 200), 
         ("/capules/valid_id", "valid_ids", 200), 
         ("/capsules/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_capsule_response_codes(self, response_code_data, route, id_type, expected_response_code):
        if route == "/capsules":
            url = self.BASE_URL
        else:
            capsule_id = ""
            if id_type == "valid_ids":
                capsule_id = response_code_data[id_type]['capsules']
            else:
                capsule_id= response_code_data[id_type]
            url = f"{self.BASE_URL}/{capsule_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"

