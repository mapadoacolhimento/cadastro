from django.conf import settings
from django.http import JsonResponse
import requests
import json
from volunteers.utils import format_phone, get_color
from volunteers.models import IntegrationLogs

url = f"{settings.ZENDESK_SUBDOMAIN}/api/v2/users/create_or_update"
password = settings.ZENDESK_API_TOKEN
username = f"{settings.ZENDESK_API_USER}/token"
ZENDESK_ORGANIZATIONS = (("psicologa", 360282119532), ("advogada", 360269610652))


def get_organization_id(type_form):
    psi, legal = ZENDESK_ORGANIZATIONS
    if type_form == psi[0]:
        return psi[1]
    return legal[1]


def create_zendesk_user(values, type_form, condition, volunteer_id):
    
 
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

        log = IntegrationLogs.objects.create(
            integration="zendesk",
            internal_id=volunteer_id,
            type="criar",
            data=json_payload,
            status="draft",
            form_type=type_form,
        )

        headers = {
            "Content-Type": "application/json",
        }

        response = requests.post(
            url, auth=(username, password), headers=headers, data=json_payload
        )

        if response.status_code  in [200,201]:
            content = json.loads(response.content)
            if response.status_code == 200:
                zendesk_user_id = content['data']['user']['id']
            else:
                zendesk_user_id = content['user']['id']

            log.external_id = zendesk_user_id
            log.status = "usuária criada"
            log.save()
            return zendesk_user_id
        else:
            # If the request is not successful, handle the error
            log.error = f"HTTP request failed with status code {response.status_code}"
            log.status = "erro"
            log.save()

    except requests.exceptions.RequestException as e:
        # Handle connection errors or timeouts
        log.error = e
        log.status = "erro"
        log.save()   
   
    except Exception as e:
        # Handle other unexpected errors
        log.error = e
        log.status = "erro"
        log.save()
    return
        