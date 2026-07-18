# SpaceX API Test Automation Suite

**Note: SpaceX API was achrived as of 6/6/2026. Daily cron job has been disabled**

## Objective
- Implement an automation suite for the publicly available [SpaceX API](https://github.com/r-spacex/SpaceX-API/tree/master), handing real engineering data and API endpoints.
- Automation testing for API response codes and schema of returned data.

## Folder / File Structure
```
root/
├── response_code_test_data/   # Contains `.yaml` file which stores 'id' values for each SpaceX entitiy. These 'id' values are used in response code testing to avoid hard coding values and enables a data-driven approach for maintainability.
├── schema_test_data/ # Stores expected schema definitions
│
└── tests/
    ├── test_response_codes/ # Contains .py files which automate response code testing.
    ├── test_schema/         # Contains `.py` files which automate schema testing.
    │  
    └── conftest.py          # Conf file for two pytest fixtures, which are used in the `.py`
                               test files to read data from provided `.yaml` files.
```
## Continuous Integration (CI) & Reporting
- Uses GitHub Actions as a CI system. 
- With each push to 'main' branch, the CI system will run through the API validation suite, catching any new issues automatically. 
- Report is generated via allure and deployed for viewing using GitHub Pages.
- ~~A 'cron' job is also ran daily at 8AM PST.~~
