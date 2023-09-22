from volunteers.moodle import moodle_api
from django.conf import settings
from volunteers.models import IntegrationLogs

def create_and_enrol(form_data):
    
    moodle_api.URL = settings.MOODLE_API_URL
    moodle_api.KEY = settings.MOODLE_API_KEY
    
    user  ={
        'firstname':form_data.values['first_name'],
        'lastname':form_data.values['last_name'],
        'email':form_data.values['email'],
        'username':form_data.values['email'],
        'auth':'manual',
        'createpassword': 1,
    }
    
    log = IntegrationLogs.objects.create(
      form_data = form_data, 
      integration = 'moodle',
      type = 'criar',
      data = user,
      status = 'draft'
    )
    
    try:
      response = moodle_api.call('core_user_create_users', users = [user])     
      log.external_data = response[0]["id"]
      log.status = 'usuária criada'
      log.save()  
    except Exception as err: 
      log.error = err
      log.status = 'erro'
      log.save()
      return False
    
    logEnrol = IntegrationLogs.objects.create(
      form_data = form_data, 
      integration = 'moddle',
      type = 'matricular',
      data = user,
      status = 'draft'
    )
    try:
      moodle_api.call('enrol_manual_enrol_users', enrolments = [{'roleid':5,'userid':response[0]["id"],'courseid':2}])
      logEnrol.external_data = response[0]["id"]
      logEnrol.status = 'usuária matriculada'
      logEnrol.save()
    except Exception as err:
      logEnrol.error = err
      logEnrol.status = 'erro'
      logEnrol.save()
      return False
    
    return True