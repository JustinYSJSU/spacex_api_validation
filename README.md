# SpaceX API Test Automation Suite

## Objective
- Implement an automation suite for the SpaceX API [Link](https://github.com/r-spacex/SpaceX-API/tree/master), handing real engineering data and API endpoints.
- Automation testing for API response codes and schema of returned data.

## Folder / File Structure
- `/response_code_test_data` -> Contains `.yaml` file which stores 'id' values for each SpaceX entitiy. These 'id' values are used in response code testing to avoid hard coding values and enables a data-driven approach for maintainability.
- `/schema_test_data` -> Contains `.yaml` files which store the expected schema for each SpaceX entity.
- `/tests` -> Contains folders + files which automate response code and schema testing.
  - `/test_response_codes` -> Contains `.py` files which automate response code testing.
  - `/test_schema` -> Contains `.py` files which automate schema testing.
  - `conftest.py` -> Conf file for two pytest fixtures, which are used in the `.py` test files to read data from provided `.yaml` files.
