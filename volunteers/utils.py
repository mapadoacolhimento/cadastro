from django.conf import settings
from django.http import JsonResponse
import requests
import json
from .models import Volunteer,VolunteerStatusHistory,VolunteerAvailability
from .choices import (
    SUPPORT_TYPE,
    OCCUPATION,
)
from datetime import datetime

from .constants import LIST_OF_REJECTED

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

def get_condition_volunteer(current_condition):
  
      if current_condition in ['inscrita',
        'reprovada_estudo_de_caso',
        'reprovada_registro_inválido',     
        'dados_incompletos_telefone',
        'reprovada_diretrizes_do_mapa',
        'not_found',
        'dados_incompletos_email',
        'descadastrada',
        'desabilitada',
        'dados_incompletos_endereço',
        'aprovada']: 
          return 'cadastrada'
      
      if current_condition in ['indisponível_outros_motivos',
       'indisponível_férias',
       'indisponivel_agenda',
       'indisponível_saude',
       'indisponível_maternidade',
       'indisponível_-sem_resposta']:
          return 'disponivel' 
        
      return current_condition
  
def create_or_update_volunteer_availability(volunteer: Volunteer):
      def get_support_type(occupation):
            psi, legal = SUPPORT_TYPE
            if occupation  == "psychologist":
                return psi[0]
            return legal[0]

      def get_offers_online_support(modality_res):
            if modality_res == "on_site":
                return False
            return True
    
      volunteer_availability = VolunteerAvailability.objects.update_or_create(
                volunteer_id=volunteer.id,
                defaults = { 
                            'max_matches': volunteer.availability,
                            'support_type':get_support_type(volunteer.occupation),
                            'support_expertise':volunteer.fields_of_work,
                            'offers_online_support':get_offers_online_support(
                              volunteer.modality
                            ),
                            'city':volunteer.city,
                            'state':volunteer.state,
                            'offers_libras_support':volunteer.offers_libras_support,
                            'lat':volunteer.latitude,
                            'lng':volunteer.longitude
                }
            )
      return volunteer_availability

def create_or_update_volunteer(form_data):
    phone = (
            form_data.values["phone"]
            .replace(" ", "")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
        )

    def get_volunteer_occupation(type_form):
            psi, legal = OCCUPATION
            if type_form == "psicologa":
                return psi[0]
            return legal[0]
          
    volunteer, created = Volunteer.objects.update_or_create( email = form_data.values["email"],
            defaults = { 
                          'occupation': get_volunteer_occupation(form_data.type_form),
                          'first_name':form_data.values["first_name"],
                          'last_name':form_data.values["last_name"],
                          'phone':phone,
                          'zipcode':form_data.values["zipcode"].replace("-", ""),
                          'state':form_data.values["state"],
                          'city':form_data.values["city"],
                          'neighborhood':form_data.values["neighborhood"],
                          'street':form_data.values["street"],
                          'register_number':form_data.values["document_number"],
                          'birth_date':datetime.strptime(form_data.values["birth_date"], "%Y-%m-%d"),
                          'color':form_data.values["color"],
                          'gender':form_data.values["gender"],
                          'modality':form_data.values["modality"],
                          'fields_of_work':form_data.values["fields_of_work"],
                          'years_of_experience':form_data.values["years_of_experience"],
                          'availability':form_data.values["availability"],
                          'offers_libras_support':form_data.values["libras"]
                        }            
        )
    
    if created:
      volunteer.condition = form_data.values["status"]
    else:
      volunteer.condition = get_condition_volunteer(volunteer.condition)
    
    if "approach" in form_data.values:
            volunteer.approach = form_data.values["approach"]
    
    if  form_data.values["lat"] != "" and form_data.values["lat"] != "" :
            volunteer.latitude=form_data.values["lat"]
            volunteer.longitude=form_data.values["lng"]
    
    volunteer.save()
    
    volunteer_status_history = VolunteerStatusHistory.objects.create(
            volunteer_id=volunteer.id,
            status=volunteer.condition,
      )
    if volunteer.condition not in LIST_OF_REJECTED: 
      create_or_update_volunteer_availability(volunteer)

    return volunteer
