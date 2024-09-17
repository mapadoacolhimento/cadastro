import unicodedata
from django.conf import settings
from django.http import JsonResponse
import requests
import json
from volunteers.utils import format_phone, get_color
from volunteers.models import IntegrationLogs

url = settings.ZENDESK_SUBDOMAIN
password = settings.ZENDESK_API_TOKEN
username = f"{settings.ZENDESK_API_USER}/token"
ZENDESK_ORGANIZATIONS = (("psicologa", 360282119532), ("advogada", 360269610652))


def get_organization_id(type_form):
    psi, legal = ZENDESK_ORGANIZATIONS
    if type_form == psi[0]:
        return psi[1]
    return legal[1]

def get_ocuppation_label(type_form):
    if type_form == "psicologa":
        return "Psicóloga"
    return "Advogada"

def format_fields_of_work(fields_of_work):
    for i,fow in enumerate(fields_of_work):
        fields_of_work[i] = unicodedata.normalize("NFD",fow.replace(" ", "_").replace("/", "_").replace("-","_")).lower()
    return fields_of_work

def create_zendesk_user(values, type_form, condition, volunteer_id):

    try:

        phone = format_phone(values['phone'])
        color = get_color(values['color'])
        payload = {
            "user": {
                "name": f"{values['first_name']} {values['last_name']}",
                "role": "end-user",
                "organization_id": get_organization_id(type_form),
                "email": values["email"].lower(),
                "phone": phone,
                "verified": True,
                "user_fields": {
                    "condition": condition,
                    "state": values['state'],
                    "city": values['city'],
                    "cep": values['zipcode'].replace("-", ""),
                    "cor": color,
                    "whatsapp": f'https://wa.me/55phone',
                    "registration_number": values['document_number'],
                    "fields_of_work": format_fields_of_work(values["fields_of_work"]),
                    "disponibilidade_de_atendimentos": values['availability'],
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
            f"{url}/api/v2/users/create_or_update", auth=(username, password), headers=headers, data=json_payload
        )

        if response.status_code  in [200,201]:
            content = json.loads(response.content)
            if 'data' in content:
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


def create_zendesk_ticket(volunteer, type_form): 
    
    try: 

        payload = { 
            "ticket": {
		        "requester_id": volunteer.zendesk_user_id,
		        "organization_id": get_organization_id(type_form),
		        "description": "Via cadastro.",
		        "subject": f"[{get_ocuppation_label(type_form)}] {volunteer.first_name} - {volunteer.register_number}",
		        "comment": {
			        "body": "Cadastrada",
			        "public": False
		        },
		        "status": "pending",
		        "custom_fields": [
			        {
				        "id": 360021879811, 
				        "value": volunteer.city
			        },
			        {
				        "id": 360021812712, 
				        "value": volunteer.phone
			        },
			        {
				        "id": 360016631592, 
				        "value": f"{volunteer.first_name} {volunteer.last_name}",
			        },
			        {
				        "id": 360021665652, 
				        "value": volunteer.condition
			        },
			        {
				        "id": 360021879791,
				    "value": volunteer.state
			        }
		        ]
	        }
        }
        
        json_payload = json.dumps(payload)
        
        log = IntegrationLogs.objects.create(
            integration="zendesk",
            internal_id=volunteer.id,
            type="ticket",
            data=json_payload,
            status="draft",
            form_type=type_form,
        )

        headers = {
            "Content-Type": "application/json",
        }
       
        response = requests.post(
            f"{url}/api/v2/tickets", auth=(username, password), headers=headers, data=json_payload
        )

        if response.ok:
            content = json.loads(response.content)
            log.data = content
            log.external_id = volunteer.zendesk_user_id
            log.status = "ticket criado"
            log.save()
            return content
        
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