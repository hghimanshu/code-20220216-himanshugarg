# BMI-Calculator
A service for calculating BMI for the given input data


# `PYTHONPATH` setup

- Set this environment variable (.env file in root for VS Code) `export PYTHONPATH=./src`


# Run Tests Locally

### Setting up Environment Variables
```bash
export DATA_FILE_PATH='configs/mockData.json'
```

where the variables used above are as below :

| Variable              | Use                               |
| :-------------------: | :-------------------------------: |
| DATA_FILE_PATH          | Json file contaning data to calculate BMI|

# Running Locally

## requirements before running local tests

- Install the required packages from poetry
```bash
poetry install
```
- Then you can run 

```bash
poetry run pytest
```

# Endpoints

### `health` endpoint
This endpoint is used to check if the server is setup correctly or not.

### `get-bmi-data` endpoint
This endpoint is used to calculate the bmi, bmi-category and health risk for the given data file.

### `get-overweight-persons` endpoint
This endpoint is used to get the total count of overweighted persons
