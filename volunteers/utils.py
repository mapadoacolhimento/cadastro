from django.conf import settings
from django.http import JsonResponse
import requests
import json
from unidecode import unidecode
from .models import Volunteer, VolunteerStatusHistory, VolunteerAvailability
from .choices import SUPPORT_TYPE, OCCUPATION, COLOR_CHOICES
from datetime import datetime

from .constants import (
    REJECTED_VOLUNTEERS,
    AVAILABLE_VOLUNTEER_CONDITION,
    ACTIVE_VOLUNTEER_CONDITION,
    ABSENT_VOLUNTEER_CONDITION,
    UNETHICAL_VOLUNTEER_CONDITION,
    REGISTERED_VOLUNTEER_CONDITION,
)


url = "https://app.loops.so/api/v1/transactional"
authorization_token = settings.LOOPS_API_KEY


def send_welcome_email(email, name):
    try:
        payload = {
            "email": email,
            "transactionalId": "clrxm539201hk267xpve25i24",
            "dataVariables": {"name": name, "email": email},
        }

        json_payload = json.dumps(payload)

        headers = {
            "Authorization": f"Bearer {authorization_token}",
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, data=json_payload)

        if response.status_code == 200:
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


def get_new_volunteer_condition(current_condition):

    if current_condition in ACTIVE_VOLUNTEER_CONDITION:
        return current_condition

    if current_condition in UNETHICAL_VOLUNTEER_CONDITION:
        return current_condition

    if current_condition in ABSENT_VOLUNTEER_CONDITION:
        return AVAILABLE_VOLUNTEER_CONDITION

    return REGISTERED_VOLUNTEER_CONDITION


def get_support_type(occupation):
    psi, legal = SUPPORT_TYPE
    if occupation == "psychologist":
        return psi[0]
    return legal[0]


def get_offers_online_support(modality_res):
    if modality_res == "on_site":
        return False
    return True


def get_color(color):
    for choice in COLOR_CHOICES:
        if choice[0] == color:
            return unidecode(choice[1].lower())
    return ""


def create_or_update_volunteer_availability(volunteer: Volunteer):

    volunteer_availability = VolunteerAvailability.objects.update_or_create(
        volunteer_id=volunteer.id,
        defaults={
            "max_matches": volunteer.availability,
            "support_type": get_support_type(volunteer.occupation),
            "support_expertise": volunteer.fields_of_work,
            "offers_online_support": get_offers_online_support(volunteer.modality),
            "city": volunteer.city,
            "state": volunteer.state,
            "offers_libras_support": volunteer.offers_libras_support,
            "lat": volunteer.latitude,
            "lng": volunteer.longitude,
            "is_available": volunteer.condition == AVAILABLE_VOLUNTEER_CONDITION,
        },
    )
    return volunteer_availability


def format_phone(phone):
    return phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")


def get_volunteer_occupation(type_form):
    psi, legal = OCCUPATION
    if type_form == "psicologa":
        return psi[0]
    return legal[0]


def create_or_update_volunteer(form_data):

    volunteer, created = Volunteer.objects.update_or_create(
        email=form_data.values["email"].lower(),
        defaults={
            "occupation": get_volunteer_occupation(form_data.type_form),
            "first_name": form_data.values["first_name"],
            "last_name": form_data.values["last_name"],
            "phone": format_phone(form_data.values["phone"]),
            "zipcode": form_data.values["zipcode"].replace("-", ""),
            "state": form_data.values["state"],
            "city": form_data.values["city"],
            "neighborhood": form_data.values["neighborhood"],
            "street": form_data.values["street"],
            "register_number": form_data.values["document_number"],
            "birth_date": datetime.strptime(form_data.values["birth_date"], "%Y-%m-%d"),
            "color": form_data.values["color"],
            "gender": form_data.values["gender"],
            "modality": form_data.values["modality"],
            "fields_of_work": form_data.values["fields_of_work"],
            "years_of_experience": form_data.values["years_of_experience"],
            "availability": form_data.values["availability"],
            "offers_libras_support": form_data.values["libras"],
        },
    )

    # se é uma voluntária nova
    if created:
        volunteer.condition = form_data.values["status"]
    else:
        volunteer.condition = get_new_volunteer_condition(volunteer.condition)

    # se a voluntária for psicóloga salva o campo da abordagem
    if "approach" in form_data.values:
        volunteer.approach = form_data.values["approach"]

    # se encontrou as coordenadas do endereço atualiza essa informação
    if form_data.values["lat"] != "" and form_data.values["lat"] != "":
        volunteer.latitude = form_data.values["lat"]
        volunteer.longitude = form_data.values["lng"]

    volunteer.save()

    volunteer_status_history = VolunteerStatusHistory.objects.create(
        volunteer_id=volunteer.id,
        status=volunteer.condition,
    )
    if volunteer.condition not in REJECTED_VOLUNTEERS:
        create_or_update_volunteer_availability(volunteer)

    return volunteer
