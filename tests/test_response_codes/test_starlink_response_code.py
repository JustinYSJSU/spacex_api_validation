import pytest
import requests

class TestResponseCodesStarlink:

    BASE_URL = "https://api.spacexdata.com/v4/starlink"

    @pytest.mark.parametrize("route, id_type, expected_response_code", 
        [("/starlink", "None", 200), 
         ("/starlink/valid_id", "valid_ids", 200), 
         ("/starlink/invalid_id", "invalid_ids", 404)])
    @pytest.mark.response_code
    def test_all_starlink_responses(self, response_code_data, route, id_type, expected_response_code):
        if route == "/starlink":
            url = self.BASE_URL
        else:
            satellite_id = ""
            if id_type == "valid_ids":
                satellite_id = response_code_data[id_type]['satellites']
            else:
                satellite_id = response_code_data[id_type]
            url = f"{self.BASE_URL}/{satellite_id}"
        response = requests.get(url)
        assert response.status_code == expected_response_code, f"Expected status code {expected_response_code} for {self.BASE_URL}, but received {response.status_code} for {url}"