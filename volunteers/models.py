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
    SUPPORT_TYPE,
    FOW_LAWYER_CHOICES,
    VOLUNTEER_STATUS,
    OCCUPATION,
)


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False

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
    external_id = models.BigIntegerField(blank=True, null=True)
    internal_id = models.BigIntegerField(blank=True, null=True)
    form_type = models.CharField(
        max_length=15,
        blank=True,
        choices=(("psicologa", "Psicóloga"), ("advogada", "Advogada"), ("msr", "Msr")),
    )
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    error = models.TextField()
    data = models.JSONField(blank=True, default=dict)

    class Meta:
        db_table = "integrations_logs"
        managed = False


class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    form_entries_id = models.BigIntegerField(null=True)
    zendesk_user_id = models.BigIntegerField(blank=True, null=True)
    moodle_id = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(
        max_length=12,
        blank=True,
        choices=OCCUPATION,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    condition = models.CharField(
        max_length=30,
        blank=True,
        choices=VOLUNTEER_STATUS,
    )
    first_name = models.CharField("Primeiro nome", max_length=200)
    last_name = models.CharField("Sobrenome", max_length=200)
    email = models.EmailField("Email")
    phone = models.CharField("Telefone de atendimento", max_length=100)
    zipcode = models.CharField("CEP", max_length=9)
    state = models.CharField("Estado", max_length=9)
    city = models.CharField("Cidade", max_length=100)
    neighborhood = models.CharField("Bairro", max_length=100)
    street = models.CharField("Rua", max_length=200, blank=True, null=True)
    latitude = models.DecimalField(
        "Latitude", max_digits=10, decimal_places=4, blank=True, null=True
    )
    longitude = models.DecimalField(
        "Longitude", max_digits=10, decimal_places=4, blank=True, null=True
    )
    register_number = models.CharField("Numero de registro", max_length=400)
    birth_date = models.DateTimeField("Data de nascimento")
    color = models.CharField(max_length=100, blank=True, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=100, blank=True, choices=COLOR_CHOICES)
    modality = models.CharField(max_length=100, blank=True, choices=MODALITY_CHOICES)
    offers_libras_support = models.BooleanField("Libras", default=False)
    fields_of_work = models.CharField(max_length=200, blank=True, choices=FOW_CHOICES)
    years_of_experience = models.CharField(
        max_length=100, blank=True, choices=YEARS_OF_EXPERIENCE_CHOICES
    )
    availability = models.IntegerField(blank=True, choices=AVAILABILITY_CHOICES)
    approach = models.CharField(
        max_length=100, blank=True, null=True, choices=APPROACH_CHOICES
    )

    form_data = models.ForeignKey("FormData", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = "volunteers"
        managed = False


class VolunteerAvailability(models.Model):
    volunteer = models.OneToOneField(
        Volunteer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="volunteer_availability",
    )
    current_matches = models.IntegerField(default=0)
    max_matches = models.IntegerField(default=1)
    is_available = models.BooleanField(default=False)
    support_type = models.CharField(max_length=20, choices=SUPPORT_TYPE)
    support_expertise = models.CharField(max_length=200, choices=FOW_CHOICES)
    offers_online_support = models.BooleanField()
    offers_libras_support = models.BooleanField()
    lat = models.DecimalField(
        "latitude", max_digits=10, decimal_places=4, blank=True, null=True
    )
    lng = models.DecimalField(
        "longitude", max_digits=10, decimal_places=4, blank=True, null=True
    )
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "volunteer_availability"
        managed = False


class VolunteerStatusHistory(models.Model):
    volunteer = models.ForeignKey("Volunteer", models.CASCADE)
    status = models.CharField(
        max_length=30,
        choices=VOLUNTEER_STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "volunteer_status_history"
        managed = False


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_value = models.CharField(max_length=100)
    city_label = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    ibge_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = "cities"
