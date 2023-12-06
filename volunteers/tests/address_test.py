import unicodedata
from unidecode import unidecode
from django.http import JsonResponse, Http404
from volunteers.views import address as address_view
import pytest
from unittest.mock import patch


@pytest.mark.django_db
@patch("volunteers.views.get_address_via_pycep")
@patch("volunteers.views.get_address_via_brasil_api")
@patch("volunteers.views.get_coordinates")
@patch("volunteers.views.get_coordinates_via_geoconding")
def test_address_view(
    mock_get_geoconding, mock_get_coordinates, mock_brasil_api, mock_pycep, rf
):
    request = rf.get("/address/", {"zipcode": "52010210"})

    # Mocking the responses from external functions
    mock_get_pycep_response = {"city": "Recife"}
    mock_get_brasil_api_response = None
    mock_get_coordinates_response = {
        "lat": 123.456,
        "lng": 789.012,
    }  # atualizar valores
    mock_get_geoconding_response = None

    mock_pycep.return_value = mock_get_pycep_response
    mock_brasil_api.return_value = mock_get_brasil_api_response
    mock_get_coordinates.return_value = mock_get_coordinates_response
    mock_get_geoconding.return_value = mock_get_geoconding_response

    response = address_view(request)

    assert response.status_code == 200
    assert isinstance(response, JsonResponse)
    assert (
        response.content.decode("utf-8")
        == '{"city": "Recife", "coordinates": {"lat": 123.456, "lng": 789.012}}'
    )

    # Test with no zipcode
    request_without_zipcode = rf.get("/address/")
    response_without_zipcode = address_view(request_without_zipcode)

    assert response_without_zipcode.status_code == 404
    assert isinstance(response_without_zipcode, Http404)
