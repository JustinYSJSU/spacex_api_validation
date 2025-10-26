import pytest
import yaml
import os

"""
Fixture to standardizer reading from the resposne_code_data.yaml file
Fixture will read the file each time it is called, eliminates duplicate code in testing response codes.
"""
@pytest.fixture(scope="module")
def response_code_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "../response_code_test_data/response_code_data.yaml")
    with open(file_path, 'r') as f:
       return yaml.load(f, Loader=yaml.SafeLoader)

"""
Pytest fixtures cannot directly take arguments from the test class
Instead, declare a _loader function within the fixture, where the parameter can be passed. 
Fixture will return this _loader function instead
"""  
@pytest.fixture(scope="module")
def schema_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    def _loader(filename):
        path = os.path.join(base_dir, f"../schema_test_data/{filename}")
        with open(path, 'r') as f:
          return yaml.load(f, Loader=yaml.SafeLoader)
    return _loader