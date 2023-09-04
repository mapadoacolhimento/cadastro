from django.db import models
from django.contrib.auth.models import User
from .choices import (
    COLOR_CHOICES,
    GENDER_CHOICES,
    APPROACH_CHOICES,
    YEARS_OF_EXPERIENCE_CHOICES,
    MODALITY_CHOICES,
    FOW_LAWYER_CHOICES,
    FOW_THERAPIST_CHOICES,
)
from datetime import datetime

class FormData(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="form_data"
    )
    type_form = models.CharField(
        max_length=10,
        blank=True,
        choices=(("psicologa", "Psicóloga"), ("advogada", "Advogada")),
    )
    total_steps = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    values = models.JSONField(blank=True, default=dict)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField('updated_date', auto_now=True)

    def __init__(self, *args, **kwargs):
        super(FormData, self).__init__(*args, **kwargs)
        if self.type_form == 'psicologa':
          self.total_steps = 12
        elif self.type_form == 'advogada':
          self.total_steps = 11

class IntegrationLogs(models.Model):
  integration = models.CharField( max_length=15,blank=True, choices = (('bonde', 'Bonde'), ('moodle','Moodle'), ('action_network','Action Network')))
  type = models.CharField(max_length=30)
  form_data = models.ForeignKey('FormData', models.CASCADE)
  created_at = models.DateTimeField(default=datetime.now)
  status = models.CharField(max_length=30)
  error = models.CharField(max_length=200)
  data = models.JSONField(blank=True, default=dict)
  external_data =  models.JSONField(blank=True, default=dict)
