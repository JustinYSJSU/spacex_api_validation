import requests
import yaml

class TestResponseCodeCompany:

    BASE_URL = "https://api.spacexdata.com/v4/roadster"

    def test_company_all(self):
        url = self.BASE_URL
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200 for {self.BASE_URL}, but received {response.status_code} for {url}"