import pytest
import yaml
import os

@pytest.fixture(scope="module")
def response_code_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "../response_code_test_data/response_code_data.yaml")
    with open(file_path, 'r') as f:
       return yaml.load(f, Loader=yaml.SafeLoader)