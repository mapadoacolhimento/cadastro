from django.db import models
from django.contrib.auth.models import User

class FormData(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "form_data")
  ocuppation = models.CharField(max_length=10, blank=True, choices=(("psicologa","Psicóloga"), ("advogada","Advogada")))
  # subscribe_status
  step = models.IntegerField(default=1)
  values = models.JSONField(blank= True, default= dict)

  # first_name
  # last_name
  # email	
  # phone	
  # whatsapp
  # zipcode
  # register_number	
  # color	
  # gender
  # day_of_birth
  # modality	
  # fields_of_work
  # years_of_experience	
  # libras	
  # approach
  # accepted_term_1	
  # accepted_term_2	
  # accepted_term_3	
  # accepted_term_4	
  # volunteer_status
  # occupation
  # state	
  # city