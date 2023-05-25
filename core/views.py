from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django import forms

from .forms import VolunteerForm
from .choices import (
    COLOR_CHOICES,
    GENDER_CHOICES,
    AVAILABILITY_CHOICES,
    MODALITY_CHOICES,
    LIBRAS_CHOICE,
    YEARS_OF_EXPERIENCE_CHOICES,
    FOW_THERAPIST_CHOICES,
    APPROACH_CHOICES,
)
from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField
from .models import FormData


# Create your views here.
step_forms = {
    1: {
        "title": "Seus Dados",
        "subtitle": "",
        "fields": {
            "first_name": CharField(label="Primeiro nome"),
            "last_name": CharField(label="Sobrenome", required=False),
            "email": EmailField(label="Seu melhor e-mail"),
            "whatsapp": MaskField(label="Número de telefone", mask="(00) 0 0000-0000"),
            "zipcode": ZipCodeField(label="CEP de atendimento", mask="00000-000"),
        },
    },
    2: {
        "title": "Seus Dados",
        "subtitle": "",
        "fields": {
            "color": ChoiceField(label="Cor", choices=COLOR_CHOICES),
            "gender": ChoiceField(label="Identidade de gênero", choices=GENDER_CHOICES),
            "phone": MaskField(
                label="Telefone de atendimento com DDD", mask="(00) 0 0000-0000"
            ),
            "document_number": MaskField(label="CRP", mask="00/000000"),
        },
    },
    3: {
        "title": "Disponibilidade",
        "subtitle": "Como voluntária, você se dispõe a atender pelo menos 1 mulher que precisa de ajuda com o mínimo de 1h de dedicação semanal. Se tiver disponibilidade, pode atender mais mulheres informando-nos abaixo:",
        "fields": {
            "aviability:": ChoiceField(
                label="Vagas para atendimento:", choices=AVAILABILITY_CHOICES
            ),
            "modality:": ChoiceField(
                label="Modalidade de atendimento", choices=MODALITY_CHOICES
            ),
            "libras:": ChoiceField(
                label="Atende em linguagem de sinais (libras)", choices=LIBRAS_CHOICE
            ),
        },
    },
    4: {
        "title": "Experiência",
        "subtitle": "Há quanto tempo você atua com acolhimento de mulheres em situação de violência?",
        "fields": {
            "years_of_experience": ChoiceField(
                label="Há quanto tempo você atua com acolhimento de mulheres em situação de violência?",
                widget=forms.RadioSelect,
                choices=YEARS_OF_EXPERIENCE_CHOICES,
            )
        },
    },
    5: {
        "title": "Campo de atuação",
        "subtitle": "",
        "fields": {
            "fields_of_work": forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple,
                choices=FOW_THERAPIST_CHOICES,
            )
        },
    },
    6: {
        "title": "Abordagem",
        "subtitle": "",
        "fields": {
            "approach": ChoiceField(
                label="Abordagem",
                widget=forms.RadioSelect,
                choices=APPROACH_CHOICES,
            )
        },
    },
    7: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_1": ChoiceField(
                label="Termo 1",
                widget=forms.RadioSelect,
                choices=((True, "Sim"), (False, "Não")),
            )
        },
    },
}


def index(request):
    return render(request=request, template_name="home.html")


def fill_step_1(request, type_form, step):
    # import ipdb;ipdb.set_trace()
    if request.user.is_authenticated:
        form_data = FormData.objects.get(user=request.user)

        if step != form_data.step + 1:
            if len(step_forms) == form_data.step:
                messages.success(
                    request,
                    "Você já preecheu o formulário! Já pode começar sua capacitação.",
                )
                return HttpResponseRedirect("/")

            return HttpResponseRedirect(f"/{type_form}/{form_data.step+1}")
    elif step != 1:
        return HttpResponseRedirect(f"/{type_form}/1")

    # import ipdb;ipdb.set_trace()
    step_form = step_forms.get(step)

    if not step_form:
        raise Exception("Etapa não existe")

    fields = step_form["fields"]

    if request.method == "POST":
        form = VolunteerForm(fields=fields, data=request.POST)

        if form.is_valid():
            if step == 1:
                user, created = User.objects.get_or_create(
                    email=form.cleaned_data["email"]
                )

                login(request, user)
                # manter usuario logado navegador
                request.session.set_expiry(0)

                form_data, created_form = FormData.objects.get_or_create(
                    user=user, ocuppation=type_form
                )
                if created_form:
                    user.username = form.cleaned_data["email"]
                    user.first_name = form.cleaned_data["first_name"]
                    user.last_name = form.cleaned_data["last_name"]
                    user.is_staff = False
                    user.save()
                else:
                    return HttpResponseRedirect(f"/{type_form}/{form_data.step+1}")

            else:
                # TODO se o passo não for 1 e não tiver usuario
                form_data = request.user.form_data

            form_data.step = step
            form_data.values = {**form_data.values, **form.cleaned_data}
            form_data.save()

            if step == list(step_forms)[-1]:
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect(f"/{type_form}/{step+1}")

    else:
        form = VolunteerForm(fields=fields)

    context = dict(
        title=step_form["title"],
        subtitle=step_form["subtitle"],
        step=step,
        form=form
    )

    return render(request, "forms/people.html", context)
