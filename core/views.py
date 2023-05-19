from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PeopleForm, People2Form, VolunteerForm
from .choices import (
    COLOR_CHOICES,
    GENDER_CHOICES,
    AVAILABILITY_CHOICES,
    MODALITY_CHOICES,
    LIBRAS_CHOICE,
)
from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField
from .auth_views import form_view
from django.contrib.auth.models import User

# Create your views here.
step_forms = {
    1: {
        "first_name": CharField(label="Primeiro nome"),
        "last_name": CharField(label="Sobrenome", required=False),
        "email": EmailField(label="Seu melhor e-mail"),
        "whatsapp": MaskField(label="Número de telefone", mask="(00) 0 0000-0000"),
        "zipcode": ZipCodeField(label="CEP de atendimento", mask="00000-000"),
    },
    2: {
        "color": ChoiceField(label="Cor", choices=COLOR_CHOICES),
        "gender": ChoiceField(label="Identidade de gênero", choices=GENDER_CHOICES),
        "phone": MaskField(
            label="Telefone de atendimento com DDD", mask="(00) 0 0000-0000"
        ),
        "document_number": MaskField(label="CRP", mask="00/000000"),
    },
    3: {
        "Vagas para atendimento:": ChoiceField(
            label="Vagas para atendimento:", choices=AVAILABILITY_CHOICES
        ),
        "Modalidade de atendimento:": ChoiceField(
            label="Modalidade de atendimento", choices=MODALITY_CHOICES
        ),
        "Atende em linguagem de sinais (libras):": ChoiceField(
            label="Atende em linguagem de sinais (libras)", choices=LIBRAS_CHOICE
        ),
    },
}

def index(request):
    return render(request=request, template_name="home.html")

def fill_step_1(request, type_form, step):
    fields = step_forms.get(step)
    if not fields:
        raise Exception("Etapa não existe")

    if request.method == "POST":
        form = VolunteerForm(fields=fields, data=request.POST)
        if form.is_valid():
            if step == list(step_forms)[-1]:
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect(f"/{type_form}/{step+1}")

    else:
        form = VolunteerForm(fields=fields)

    return render(request, "forms/people.html", {"form": form})
