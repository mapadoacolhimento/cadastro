from django.db import models
from django.contrib.auth.models import User
from .choices import COLOR_CHOICES, GENDER_CHOICES,APPROACH_CHOICES,YEARS_OF_EXPERIENCE_CHOICES, MODALITY_CHOICES, FOW_LAWYER_CHOICES, FOW_THERAPIST_CHOICES
class FormData(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "form_data")
  type_form = models.CharField(max_length=10, blank=True, choices=(("psicologa","Psicóloga"), ("advogada","Advogada")))
  # subscribe_status
  step = models.IntegerField(default=1)
  values = models.JSONField(blank= True, default= dict)

# FOW_CHOICES = FOW_THERAPIST_CHOICES + FOW_LAWYER_CHOICES
# class Volunteer(models.Model):
  
#   first_name =  models.CharField(max_length=30)
#   last_name =  models.CharField(max_length=30)
#   occupation = models.CharField(max_length=10, blank=True, choices=(("psicologa","Psicóloga"), ("advogada","Advogada")))
#   email	= models.EmailField()
#   phone	= models.CharField(max_length=11)
#   whatsapp = models.CharField(max_length=11)
#   #TODO  pegar as informações de endereço?
#   zipcode = models.CharField(max_length=8)
#   register_number	=  models.CharField(max_length=15)
#   color	= models.CharField(max_length=10, blank=True, choices=COLOR_CHOICES)
#   gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
#   modality = models.CharField(max_length=10, blank=True, choices=MODALITY_CHOICES)
#   fields_of_work = models.CharField(max_length=10, blank=True, choices=FOW_CHOICES)
#   years_of_experience	=models.CharField(max_length=10, blank=True, choices= YEARS_OF_EXPERIENCE_CHOICES)
#   libras	= models.BooleanField(default=False)
#   approach = models.CharField(max_length=10, blank=True, choices=APPROACH_CHOICES)
#   volunteer_status = models.CharField(max_length=10, blank=True, choices=(("cadastrada","CADASTRADA"), ("reprovada_diretrizes","REPROVADA_DIRETRIZES")))
