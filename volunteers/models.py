from django.db import models
from django.contrib.auth.models import User
from .choices import (
    COLOR_CHOICES,
    GENDER_CHOICES,
    APPROACH_CHOICES,
    YEARS_OF_EXPERIENCE_CHOICES,
    MODALITY_CHOICES,
    FOW_CHOICES,
    AVAILABILITY_CHOICES,
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
    updated_at = models.DateTimeField("updated_date", auto_now=True)

    def __init__(self, *args, **kwargs):
        super(FormData, self).__init__(*args, **kwargs)
        if self.type_form == "psicologa":
            self.total_steps = 12
        elif self.type_form == "advogada":
            self.total_steps = 11


class IntegrationLogs(models.Model):
    integration = models.CharField(
        max_length=15,
        blank=True,
        choices=(("bonde", "Bonde"), ("moodle", "Moodle"), ("zendesk", "Zendesk")),
    )
    external_id = models.IntegerField(blank=True, null=True)
    internal_id = models.IntegerField(blank=True, null=True)
    form_type = models.CharField(
        max_length=15,
        blank=True,
        choices=(("psicologa", "Psicóloga"), ("advogada", "Advogada"), ("msr", "Msr")),
    )
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=30)
    error = models.CharField(max_length=200)
    data = models.JSONField(blank=True, default=dict)

    class Meta:
        db_table = "integrations_logs"


class Volunteer(models.Model):
    id = models.IntegerField(primary_key=True)
    moodle_id = models.IntegerField(blank=True, null=True)
    ocuppation = models.CharField(
        max_length=10,
        blank=True,
        choices=(("psicologa", "Psicóloga"), ("advogada", "Advogada")),
    )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField("updated_date", auto_now=True)
    condition = models.CharField(
        max_length=30,
        blank=True,
        choices=(
            ("cadastrada", "cadastrada"),
            ("reprovada_diretrizes", "reprovada_diretrizes"),
        ),
    )
    first_name = models.CharField("Primeiro nome", max_length=200)
    last_name = models.CharField("Sobrenome", max_length=200)
    email = models.EmailField("Email")
    phone = models.CharField("Telefone de atendimento", max_length=11)
    whatsapp = models.CharField("Whatsapp", max_length=11)
    zipcode = models.CharField("CEP", max_length=9)
    state = models.CharField("Estado", max_length=2)
    city = models.CharField("Cidade", max_length=100)
    neighborhood = models.CharField("Bairro", max_length=100)
    latitude = models.DecimalField(
        "Latitude", max_digits=10, decimal_places=4, blank=True, null=True
    )
    logintude = models.DecimalField(
        "Longitude", max_digits=10, decimal_places=4, blank=True, null=True
    )
    register_number = models.CharField("Numero de registro", max_length=11)
    birth_date = models.DateTimeField("Data de nascimento")
    color = models.CharField(max_length=100, blank=True, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=100, blank=True, choices=COLOR_CHOICES)
    modality = models.CharField(max_length=100, blank=True, choices=MODALITY_CHOICES)
    fields_of_work = models.CharField(max_length=200, blank=True, choices=FOW_CHOICES)
    years_of_experience = models.CharField(
        max_length=100, blank=True, choices=YEARS_OF_EXPERIENCE_CHOICES
    )
    aviability = models.CharField(
        max_length=100, blank=True, choices=AVAILABILITY_CHOICES
    )
    approach = models.CharField(
        max_length=100, blank=True, null=True, choices=APPROACH_CHOICES
    )
    # disponível match reverso
    # disponível match

    form_data = models.ForeignKey("FormData", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "volunteers"
