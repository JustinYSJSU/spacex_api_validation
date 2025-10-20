import requests
import yaml

class TestResponseCodeCapsules:

    BASE_URL = "https://api.spacexdata.com/v4/capsules" # "Base" API URL for SpaceX Capsules. All tested routes use this URL or an extended version

    def test_get_all_capsules(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected response code 200, but received {response.status_code} for {url}"
        
    def test_valid_capsule_id(self, response_code_data):
        valid_capsule_id = response_code_data['valid_ids']['capsules']
        url = f"{self.BASE_URL}/{valid_capsule_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected response code 200, but received {response.status_code} for {url}"
        
    def test_invalid_capsule_id(self, response_code_data):
        invalid_capsule_id = response_code_data['invalid_ids']['generic_invalid']
        url = f"{self.BASE_URL}/{invalid_capsule_id}"
        response = requests.get(url)
        assert response.status_code == 404, f"Expected response code 404, but received {response.status_code} for {url}"
