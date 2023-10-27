# Create your views here.
from collections import ChainMap
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from .forms_screening import MsrStep0, MsrStep1, MsrStep2, MsrStep3, MsrStep4, MsrStep5, MsrStep6, MsrStep7, MsrStep8, MsrStep9, MsrStep10, MsrStep11, MsrStep12, MsrStep13, MsrStep14, MsrStep15
from .forms_register import RegisterStep0, RegisterStep1, RegisterStep2, RegisterStep3, RegisterStep4, RegisterStep5, RegisterStep6, RegisterStep7, RegisterStep8, RegisterStep9

from django.shortcuts import render, redirect
from django.db import transaction

from .models import FormData
from formtools.wizard.views import SessionWizardView


def main(request):
    template = loader.get_template("msrs/forms/screening_home.html")
    return HttpResponse(template.render())

# Wizard Form
STEP_ZERO = "0"
STEP_ONE = "1"
STEP_TWO = "2"
STEP_THREE = "3"
STEP_FOUR = "4"
STEP_FIVE = "5"
STEP_SIX = "6"
STEP_SEVEN = "7"
STEP_EIGHT = "8"
STEP_NINE = "9"
STEP_TEN = "10"
STEP_ELEVEN = "11"
STEP_TWELVE = "12"
STEP_THIRTEEN = "13"
STEP_FOURTEEN = "14"
STEP_FIFTEEN = "15"

def check_one(wizard):
    form_data = wizard.get_cleaned_data_for_step(STEP_ZERO)

    if form_data and form_data["gender_select"] == "nda":
        return False
    else:
        return True

def check_two(wizard):
    if not check_one(wizard):
        return False

    form_data = wizard.get_cleaned_data_for_step(STEP_ONE)

    if form_data and form_data["majority"] == "menor":
        return False
    else:
        return True

def check_three(wizard):
    if not check_two(wizard):
        return False

    form_data = wizard.get_cleaned_data_for_step(STEP_TWO) or {}
    if form_data and form_data["locality"] == "internacional":
        return False
    else:
        return True

def check_agree(wizard):
    form_data = wizard.get_cleaned_data_for_step(STEP_THREE) or {}

    if form_data and form_data.get("agree") == "sim":
        return True
    else:
        return False

#     Comportamento:
# CCaso ela responda até 3 salários mínimos (R$3.960,00), ela não precisará responder as outras perguntas.
def check_income(wizard):
    if not check_three(wizard):
        return False

    form_data = wizard.get_cleaned_data_for_step(STEP_ELEVEN)

    if form_data:
        income = float(form_data["income"])
        if income <= 3960:
            return False

    return True


# Caso ela responda que ganha cinco salários mínimos ou mais (R$6.600,00 ou mais), ela precisará responder todas as seguintes perguntas
def check_income_2(wizard):
    if not check_income(wizard):
        return False

    form_data = wizard.get_cleaned_data_for_step(STEP_ELEVEN)

    if form_data:
        income = float(form_data["income"])
        if income <= 6600:
            return False

    return True


def return_true(wizard):
    return True


class FormWizardView(SessionWizardView):
    template_name = "msrs/forms/screening_wizard_form.html"

    condition_dict = {
        STEP_ZERO: return_true,
        STEP_ONE: check_one,
        STEP_TWO: check_two,
        STEP_THREE: check_three,
        STEP_FOUR: check_three,
        STEP_FIVE: check_three,
        STEP_SIX: check_three,
        STEP_SEVEN: check_three,
        STEP_EIGHT: check_three,
        STEP_NINE: check_three,
        STEP_TEN: check_three,
        STEP_ELEVEN: check_three,
        STEP_TWELVE: check_income,
        STEP_THIRTEEN: check_income,
        STEP_FOURTEEN: check_income_2,
        STEP_FIFTEEN: check_income_2
    }

    form_list = [
        (STEP_ZERO, MsrStep0),
        (STEP_ONE, MsrStep1),
        (STEP_TWO, MsrStep2),
        (STEP_THREE, MsrStep3),
        (STEP_FOUR, MsrStep4),
        (STEP_FIVE, MsrStep5),
        (STEP_SIX, MsrStep6),
        (STEP_SEVEN, MsrStep7),
        (STEP_EIGHT, MsrStep8),
        (STEP_NINE, MsrStep9),
        (STEP_TEN, MsrStep10),
        (STEP_ELEVEN, MsrStep11),
        (STEP_TWELVE, MsrStep12),
        (STEP_THIRTEEN, MsrStep13),
        (STEP_FOURTEEN, MsrStep14),
        (STEP_FIFTEEN, MsrStep15),
    ]

    def process_step(self, form):
        return self.get_form_step_data(form)

    transaction.atomic

    def done(self, form_list, **kwargs):
        values = list(map(lambda form: form.cleaned_data, form_list))
        values = dict(ChainMap(*values))
        form_data = FormData.objects.create(values=values)

        total_steps = len(form_list)


        if total_steps <= 3:
            return redirect("denail", type="personal")

        income = float(values["income"])
        if income >= 6600:
            if (
                values["has_dependents"] == "Não"
                or values["financially_responsible"] == "Não"
                or values["properties"] == "Sim"
            ):
                return redirect("denail", type="socioeconomic")

        else:
            return redirect("register_home", form_data_id=form_data.id)


def denail(request, type):
    if type == "personal":
        template = loader.get_template("msrs/forms/screening_denied.html")
    elif type == "socioeconomic":
        template = loader.get_template("msrs/forms/screening_denied_socioeconomic.html")

    return HttpResponse(template.render())

class RegisterFormView(View):
    template_name = "msrs/forms/register_form.html"
    form_classes = [
        RegisterStep0,
        RegisterStep1,
        RegisterStep2,
        RegisterStep3,
        RegisterStep4,
        RegisterStep5,
        RegisterStep6,
        RegisterStep7,
        RegisterStep8,
        RegisterStep9,
    ]

    def get(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class()

        titulo = form.titulo
        subtitulo = form.subtitulo

        return render(
            request,
            self.template_name,
            {"form": form, "step": step, "titulo": titulo, "subtitulo": subtitulo},
        )

    def post(self, request, step=0, *args, **kwargs):
        form_class = self.form_classes[step]
        form = form_class(request.POST)
        if form.is_valid():
            # Armazenando dados do formulário em algum lugar
            # Avançar para a próxima etapa
            # Usando sessão:
            form_data = form.cleaned_data

            if "form_data" not in request.session:
                request.session["form_data"] = {}
            request.session["form_data"].update(form_data)
            request.session.modified = True

            if step <= 8:  # Consertar lógica final
                return redirect("register_form", step=step + 1)

        return render(request, self.template_name, {"form": form, "step": step})

def loading(request,form_data_id):
    template = loader.get_template("msrs/forms/screening_load.html")
    return HttpResponse(template.render())

def register_home(request,form_data_id):
    template = loader.get_template("msrs/forms/register_home.html")
    return HttpResponse(template.render())
