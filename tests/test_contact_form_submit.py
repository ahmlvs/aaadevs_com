import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from main import app
from db.models import ContactFormModel
from datetime import datetime, timedelta

client = TestClient(app)


# Test form validation failure
def test_contact_form_submit_validation_error():
    response = client.post(
        "/api/v1/contact_form_submit",
        data={"name": "Test John Doe", "email": "invalid-email"}
    )

    assert response.status_code == 400
    assert response.json() == {"message": "Incorrect form data!"}
