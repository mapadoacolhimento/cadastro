from django.conf import settings
from django.http import JsonResponse
import requests
import json
from volunteers.utils import format_phone, get_color

url = f"{settings.ZENDESK_SUBDOMAIN}/api/v2/users/create_or_update"
password = settings.ZENDESK_API_TOKEN
username = f"{settings.ZENDESK_API_USER}/token"
ZENDESK_ORGANIZATIONS = (("psicologa", 360282119532), ("advogada", 360269610652))


def get_organization_id(type_form):
    psi, legal = ZENDESK_ORGANIZATIONS
    if type_form == psi[0]:
        return psi[1]
    return legal[1]


def create_zendesk_user(values, type_form, condition):
    
 
    try:

        phone = format_phone(values['phone'])
        color = get_color(values['color'])
        payload = {
            "user": {
                "name": f"{values['first_name']} {values['last_name']}",
                "role": "end-user",
                "organization_id": get_organization_id(type_form),
                "email": values['email'],
                "phone": phone,
                "verified": True,
                "user_fields": {
                    "condition": condition,
                    "state": values['state'],
                    "city": values['city'],
                    "cep": values['zipcode'].replace("-", ""),
                    "address": values['street'],
                    "cor": color,
                    "whatsapp": phone,
                    "registration_number": values['document_number'],
                    "occupation_area": "",
                    "disponibilidade_de_atendimentos": values['availability'],
                    "latitude": values['lat'],
                    "longitude": values['lng'],
                },
            }
        }

        json_payload = json.dumps(payload)

        headers = {
            "Content-Type": "application/json",
        }

        print(f"url: {url}")
        print(f"auth: {username} {password}")
        print(f"payload: {json_payload}")
        
        response = requests.post(
            url, auth=(username, password), headers=headers, data=json_payload
        )

        if response.status_code  in [200,201]:
            print({"data": response.json()})
            return JsonResponse({"data": response.json()})
        else:
            # If the request is not successful, handle the error
            return JsonResponse(
                {
                    "error": f"HTTP request failed with status code {response.status_code}"
                },
                status=response.status_code,
            )
    except requests.exceptions.RequestException as e:
        # Handle connection errors or timeouts
        return JsonResponse({"error": f"HTTP request failed: {e}"}, status=500)
    except Exception as e:
        # Handle other unexpected errors
        return JsonResponse({"error": f"An unexpected error occurred: {e}"}, status=500)