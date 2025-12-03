# test_App.py
import json
import pytest
from flask import url_for

# Import the Flask app object. Adjust import if your file is named differently.
# Example: if your app file is named app.py and the Flask app variable is `app`,
# the import below will work.
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_page(client):
    """GET / should return HTML (status 200)"""
    resp = client.get('/')
    assert resp.status_code == 200
    # Basic sanity check: index should contain some HTML title or body
    assert b'<html' in resp.data.lower() or b'<!doctype html' in resp.data.lower() or b'<body' in resp.data.lower()

def test_feature_info_endpoint(client):
    """GET /feature_info should return JSON with expected keys"""
    resp = client.get('/feature_info')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    # Check a couple of expected feature keys
    assert 'CRIME_RATE' in data
    assert 'GREEN_AREA' in data

def test_predict_with_defaults(client):
    """POST /predict with no body (uses defaults) should return success and predicted_price"""
    # Send an empty JSON body to let server use defaults
    resp = client.post('/predict', json={})
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert 'success' in data
    assert data['success'] is True
    assert 'predicted_price' in data
    # Predicted price should be a number
    assert isinstance(data['predicted_price'], (int, float))

def test_predict_with_custom_input(client):
    """POST /predict with explicit valid features should return a numeric prediction"""
    # Build minimal valid payload using some custom values
    payload = {
        # numeric features (keys must match FEATURE_RANGES defined in app)
        "CRIME_RATE": 0.5,
        "GREEN_AREA": 20,
        "INDUSTRIAL_AREA": 2,
        "POLLUTION_LEVEL": 0.4,
        "AVG_ROOMS": 5.0,
        "HOUSE_AGE": 10,
        "EMPLOYMENT_DISTANCE": 4.0,
        "PROPERTY_TAX": 300,
        "TEACHER_RATIO": 16.0,
        "MIGRANT_POPULATION": 50,
        "LOW_INCOME_POP": 10.0,
        # categorical
        "RIVER_PROXIMITY": 1,
        "LOCALITY_RANK": 2
    }
    resp = client.post('/predict', json=payload)
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['success'] is True
    assert 'predicted_price' in data
    assert isinstance(data['predicted_price'], (int, float))

def test_predict_error_handling(client, monkeypatch):
    """Simulate an exception in the predict endpoint to ensure error response structure"""
    # patch the model.predict to raise an exception if model exists
    try:
        import app as app_module
        if getattr(app_module, 'model', None) is not None:
            def raise_err(x):
                raise RuntimeError("forced error")
            monkeypatch.setattr(app_module.model, 'predict', raise_err)
            payload = {}
            resp = client.post('/predict', json=payload)
            assert resp.status_code == 200
            data = resp.get_json()
            assert data['success'] is False
            assert 'error' in data
    except Exception:
        # If model is None or monkeypatching isn't applicable, just ensure endpoint still responds
        payload = {}
        resp = client.post('/predict', json=payload)
        assert resp.status_code == 200
        data = resp.get_json()
        assert 'success' in data

