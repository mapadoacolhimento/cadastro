from django.http import JsonResponse, Http404
from volunteers.views import address as address_view
import pytest
from unittest.mock import patch


@pytest.mark.django_db
def test_address_view(rf):
    zipcode_value = "52010210"
    request = rf.get("/address/", {"zipcode": zipcode_value, "city": "Recife"})

    # Mocking the responses from external functions
    mock_get_pycep_response = {"city": "Recife"}
    mock_get_brasil_api_response = None
    mock_get_coordinates_response = {
        "lat": -8.058,
        "lng": -34.883,
    }
    mock_get_geocoding_response = None

    with patch("volunteers.views.get_address_via_pycep") as mock_pycep, patch(
        "volunteers.views.get_address_via_brasil_api"
    ) as mock_brasil_api, patch(
        "volunteers.views.get_coordinates_via_geocoding"
    ) as mock_geocoding, patch(
        "volunteers.views.get_coordinates_via_google_api"
    ) as mock_google_api, patch(
        "volunteers.views.get_coordinates"
    ) as mock_get_coordinates:
        mock_pycep.return_value = mock_get_pycep_response
        mock_brasil_api.return_value = mock_get_brasil_api_response
        mock_geocoding.return_value = mock_get_geocoding_response
        mock_google_api.return_value = mock_get_coordinates_response
        mock_get_coordinates.return_value = mock_get_coordinates_response

        response = address_view(request)

        assert response.status_code == 200
        assert isinstance(response, JsonResponse)
        assert (
            response.content.decode("utf-8")
            == '{"city": "RECIFE", "coordinates": {"lat": -8.058, "lng": -34.883}}'
        )

        mock_get_coordinates.assert_not_called()

    # No zipcode
    request_without_zipcode = rf.get("/address/")
    response_without_zipcode = address_view(request_without_zipcode)

    # When there is no zipcode, the view returns None
    assert response_without_zipcode is None
