import urllib.parse
import requests
from geopy.geocoders import Nominatim
import brazilcep

from django.conf import settings


def validate_cep(field):
    cep = "".join(field.replace("-", " ").split())
    if cep.isdigit() and len(cep) == 8:
        return cep
    raise Exception('CEP "{field}" Format Invalid'.format(field=field))


def get_coordinates(address):
    geolocator = Nominatim(user_agent="geolocalização")
    if "street" in address:
        formartAddress = f"{address['street']}, {address['city']}-{address['neighborhood']}-{address['state']}-BR"
    else:
        formartAddress = (
            f"{address['city']}-{address['neighborhood']}-{address['state']}-BR"
        )
    try:
        localizacao = geolocator.geocode(formartAddress)

        return {
            "lat": round(localizacao.latitude, 3),
            "lng": round(localizacao.longitude, 3),
        }
    except Exception as error:
        print(error)
        return None


def get_coordinates_via_geoconding(address):
    apikey = settings.GEOCODING_API_KEY
    apiUrl = "https://api.opencagedata.com/geocode/v1/json"

    if "street" in address:
        formatAddress = f"{address['street']}, {address['neighborhood']}, {address['city']}, {address['state']}"
    else:
        formatAddress = (
            f"{address['neighborhood']}, {address['city']}, {address['state']}"
        )
    requestUrl = f"{apiUrl}?key={apikey}&q={urllib.parse.quote(formatAddress)}&countrycode=br&pretty=1&no_annotations=1"

    response = requests.get(requestUrl)
    if response.status_code != 200:
        return None

    results = response.json()["results"][0]
    if results:
        return {
            "lat": round(results["geometry"]["lat"], 3),
            "lng": round(results["geometry"]["lng"], 3),
        }
    return None


def get_address_via_brasil_api(zipcode):
    zipcode = validate_cep(zipcode)
    response = requests.get("https://brasilapi.com.br/api/cep/v1/" + zipcode)
    if response.status_code != 200:
        return None
    address = response.json()
    return {
        "zipcode": address["cep"],
        "state": address["state"],
        "city": address["city"],
        "neighborhood": address["neighborhood"],
        "street": address["street"],
    }


def get_address_via_pycep(zipcode):
    zipcode = validate_cep(zipcode)
    try:
        address = brazilcep.get_address_from_cep(zipcode)
        return {
            "zipcode": address["cep"],
            "state": address["uf"],
            "city": address["city"],
            "neighborhood": address["district"],
            "street": address["street"],
        }
    except:
        return None
