from django.db import models

from datetime import datetime

from volunteers.models import Cities

from .choices import (
    COLOR_CHOICES,
    GENDER_CHOICES,
    AGE_CHOICES,
    LOCAL_CHOICES,
    PHYSICAL_VIOLENCE_CHOICES,
    PSYCH_VIOLENCE_CHOICES,
    SEXUAL_VIOLENCE_CHOICES,
    DIGITAL_VIOLENCE_CHOICES,
    PROPERTY_VIOLENCE_CHOICES,
    OBSTETRIC_VIOLENCE_CHOICES,
    SERVICE_CHOICES,
    INCOME_CHOICES,
    TO_HAVE_CHOICES,
    TO_BE_CHOICES,
    TYPE_OF_SUPPORT,
    EDUCATION_CHOICES,
    DURATION_CHOICES,
    AUTHOR_CHOICES,
    RISK_CHOICES,
    PROTECTIVE_CHOICES,
    PUBLIC_SERVICE_CHOICES,
    STATUS_CHOICES,
    ACCESS_CHOICES,
    PRIORITY_CHOICES,
)


class FormData(models.Model):
    stage = models.CharField(
        max_length=20,
        blank=True,
        choices=(("triagem", "Triagem"), ("cadastro", "Cadastro")),
    )
    values = models.JSONField(blank=True, default=dict)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField("updated_date", auto_now=True)


class Msrs(models.Model):
    user_zendesk_id = models.IntegerField(blank=True, null=True)
    name = models.CharField("Nome", max_length=100)
    email = models.EmailField("Email")
    cpf = models.CharField("CPF", max_length=11)
    color = models.CharField(max_length=15, blank=True, choices=COLOR_CHOICES)
    gender = models.CharField(max_length=15, blank=True, choices=GENDER_CHOICES)
    whatsapp = models.CharField("Whatsapp", max_length=11)
    state = models.CharField("Estado", max_length=2)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name="Cidade")
    neighborhood = models.CharField("Bairro", max_length=100)
    latitude = models.DecimalField("Latitude", max_digits=10, decimal_places=4)
    logintude = models.DecimalField("Longitude", max_digits=10, decimal_places=4)
    pcd = models.BooleanField(default=False)
    education = models.CharField(
        "Nível de escolaridade", max_length=40, blank=True, choices=EDUCATION_CHOICES
    )
    work_situation = models.CharField(
        "Situação de trabalho", max_length=40, blank=True, choices=INCOME_CHOICES
    )
    income = models.DecimalField("Renda", max_digits=10, decimal_places=2)
    physical_violence = models.CharField(
        "Tipo de violência física",
        max_length=100,
        blank=True,
        choices=PHYSICAL_VIOLENCE_CHOICES,
    )
    psych_violence = models.CharField(
        "Tipo de violência psicológica",
        max_length=100,
        blank=True,
        choices=PSYCH_VIOLENCE_CHOICES,
    )
    sexual_violence = models.CharField(
        "Tipo de violência sexual",
        max_length=100,
        blank=True,
        choices=SEXUAL_VIOLENCE_CHOICES,
    )
    digital_violence = models.CharField(
        "Tipo de violência digital",
        max_length=200,
        blank=True,
        choices=DIGITAL_VIOLENCE_CHOICES,
    )
    property_violence = models.CharField(
        "Tipo de violência patrimonial",
        max_length=100,
        blank=True,
        choices=PROPERTY_VIOLENCE_CHOICES,
    )
    obstetric_violence = models.CharField(
        "Tipo de violência obstétrica",
        max_length=100,
        blank=True,
        choices=OBSTETRIC_VIOLENCE_CHOICES,
    )
    duration_of_violence = models.CharField(
        "Duração da violência", max_length=30, blank=True, choices=DURATION_CHOICES
    )
    author_of_violence = models.CharField(
        "Autor da violência", max_length=30, blank=True, choices=AUTHOR_CHOICES
    )
    story = models.TextField("Relato")
    risk_factors = models.CharField(
        "Fatores de Risco", max_length=140, blank=True, choices=RISK_CHOICES
    )
    protective_factors = models.CharField(
        "Fatores de proteção", max_length=100, blank=True, choices=PROTECTIVE_CHOICES
    )
    public_service = models.CharField(
        "Serviços públicos", max_length=100, blank=True, choices=PUBLIC_SERVICE_CHOICES
    )
    type_of_support = models.CharField(
        "Tipo de acolhimento", max_length=20, blank=True, choices=TYPE_OF_SUPPORT
    )
    access = models.CharField(
        "Como teve acesso ao Mapa", max_length=30, blank=True, choices=ACCESS_CHOICES
    )
    status = models.CharField(
        "Status da inscrição", max_length=15, blank=True, choices=STATUS_CHOICES
    )
    support_on_queue = models.BooleanField(
        "Tipos de acolhimento na fila", default=False
    )
    on_queue = models.BooleanField("Fila para o match", default=False)
    online = models.BooleanField("Aceita atendimento online", default=False)
    priority = models.CharField(max_length=15, blank=True, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField("Data da inscrição", default=datetime.now)
    updated_at = models.DateTimeField("updated_date", auto_now=True)
    match = models.BooleanField("Vai pro match", default=False)


# class Place(models.Model):
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=2, null=True)

#     def __str__(self):
#         return f"{self.city}, {self.state}"
