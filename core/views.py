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
    FOW_LAWYER_CHOICES,
    APPROACH_CHOICES,
    TERM_CHOICES,
)
from .fields import CharField, ChoiceField, EmailField, MaskField, ZipCodeField
from .models import FormData


# Create your views here.
form_steps = {
    1: {
        "title": "Seus Dados",
        "subtitle": "",
        "fields": {
            "first_name": CharField(label="Primeiro nome"),
            "last_name": CharField(label="Sobrenome", required=False),
            "email": EmailField(label="Seu melhor e-mail"),
            "whatsapp": MaskField(label="Número de telefone", mask="(00) 0 0000-0000", min_length=14),
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
                label="Telefone de atendimento com DDD", mask="(00) 0 0000-0000", min_length=14),
            "document_number": MaskField(label="CRP", mask="00/000000", min_length=8)
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
                label="Termo 1", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
    8: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_2": ChoiceField(
                label="Termo 2", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
    9: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_3": ChoiceField(
                label="Termo 3", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
    10: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_4": ChoiceField(
                label="Termo 4", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
}

TOTAL_THERAPIST = 11
TOTAL_LAYWER = 10

def current_step(step, type_form):
    if step in [1, 3, 4]:
        return form_steps.get(step)
    if step == 2:
        if type_form == "psicologa":
            form_step_2 = form_steps.get(step)
        else:
            form_step_2 = form_steps.get(step)
            form_step_2["fields"]["document_number"] = MaskField(
                label="OAB", mask="000000"
            )
        return form_step_2
    elif step == 5:
        form_step_5 = form_steps.get(step)
        if type_form == "advogada":
            form_step_5["fields"]["fields_of_work"] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple,
                choices=FOW_LAWYER_CHOICES,
            )
        return form_step_5

    elif step >= 6:
        if type_form == "psicologa":
            return form_steps.get(step)
        elif type_form == "advogada":
            return form_steps.get(step + 1)
    else:
        return None



def index(request):
    return render(request=request, template_name="home.html")


def fill_step(request, type_form, step):
  
    if type_form == 'psicologa':
        total = TOTAL_THERAPIST
    else:
        total = TOTAL_LAYWER

    if request.user.is_authenticated:
        form_data = FormData.objects.get(user=request.user)
        
        if form_data.type_form != type_form:
        #TODO entender quando uma voluntaria logada se inscreve como duas ocupações com mesmo email  
          messages.success(
            request,
            "Você já preecheu o formulário como " + form_data.type_form,
          )
          return HttpResponseRedirect("/")

        if step != form_data.step + 1:
            if total == form_data.step:
                return HttpResponseRedirect(f"/{type_form}/final/")

            return HttpResponseRedirect(f"/{type_form}/{form_data.step+1}")
        elif step == total:
            return HttpResponseRedirect(f"/{type_form}/final/")
        


    elif step != 1:
        return HttpResponseRedirect(f"/{type_form}/1")

    step_form = current_step(step, type_form)

    if not step_form:
        raise Exception("Etapa não existe")

    fields = step_form["fields"]

    if request.method == "POST":
        form = VolunteerForm(fields=fields, data=request.POST)

        if form.is_valid():
            if step == 1:
                user, created = User.objects.get_or_create(
                    username = form.cleaned_data["email"] + '-' + type_form
                )

                login(request, user)
                # manter usuario logado navegador
                request.session.set_expiry(0)

                form_data, created_form = FormData.objects.get_or_create(
                    user=user, type_form=type_form
                )
                if created_form:
                    user.username = form.cleaned_data["email"] + '-' + type_form
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

            if step == total:
                return HttpResponseRedirect(f"/{type_form}/final/")
            else:
                return HttpResponseRedirect(f"/{type_form}/{step+1}")

    else:
        form = VolunteerForm(fields=fields)

    context = dict(
        title=step_form["title"],
        subtitle=step_form["subtitle"],
        step=step,
        type_form=type_form,
        form=form,
    )

    return render(request, "forms/people.html", context)


def final_step(request, type_form):

    if type_form == 'psicologa':
        total = TOTAL_THERAPIST
    else:
        total = TOTAL_LAYWER

    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")

    form_data = FormData.objects.get(user=request.user)
    if form_data.step == total:
        messages.success(
            request,
            "Você já preecheu o formulário! Já pode começar sua capacitação.",
        )
        return HttpResponseRedirect("/")

    context = dict(step=total, form=request.user.form_data)

    if request.method == "POST":
        # salvar voluntaria com status cadastrada/aprovada
        # capacitação

        form_data.step = total
        # form_data.values["status"] = "finalizado"
        form_data.save()
        return HttpResponseRedirect("/")

    return render(request, "forms/people2.html", context)
