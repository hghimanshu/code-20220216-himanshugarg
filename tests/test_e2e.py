import pytest
from fastapi.testclient import TestClient
from bmi_calculator.server import app

def test_logger_setup():
    with TestClient(app) as test_client:
        response = test_client.get("/health")
    assert response.status_code == 200


def test_for_overweight_count():
    with TestClient(app) as test_client:
        response = test_client.get("get-overweight-persons")

    assert response.status_code == 200
    assert response.json() == 1


def test_inserting_new_columns():

    with TestClient(app) as test_client:
        response = test_client.get("get-bmi-data")

    assert response.status_code == 200
    assert len(response.json()) == 1

    for doc in response.json():
        assert len(doc) == 6
        assert "BMI" in doc.keys()
        assert "BMI-Category" in doc.keys()
        assert "Health-Risk" in doc.keys()
        
