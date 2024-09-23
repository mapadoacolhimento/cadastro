from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.conf import settings
from django import forms

from unidecode import unidecode
import unicodedata
import traceback

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
from msrs.choices import STATE_CHOICES

from .fields import (
    CharField,
    ChoiceField,
    EmailField,
    MaskField,
    ZipCodeField,
    DateField,
    SelectField,
    CustomLogicField,
)
from .models import (
    FormData,
)

from .moodle.moodle import create_and_enroll

from .address_search import (
    get_address_via_brasil_api,
    get_address_via_pycep,
    get_coordinates,
    get_coordinates_via_geocoding,
    get_coordinates_via_google_api,
)

from .utils import send_welcome_email, create_or_update_volunteer

from .constants import REJECTED_VOLUNTEERS

from volunteers.zendesk import create_zendesk_user, create_zendesk_ticket

# Create your views here.
form_steps = {
    1: {
        "title": "Seus Dados",
        "subtitle": "",
        "fields": {
            "first_name": CharField(
                label="Primeiro nome",
                widget=forms.TextInput(attrs={"aria-labelledby": "label_first_name"}),
            ),
            "last_name": CharField(
                label="Sobrenome",
                required=False,
                widget=forms.TextInput(attrs={"aria-labelledby": "label_last_name"}),
            ),
            "email": EmailField(
                label="Seu melhor e-mail",
                widget=forms.EmailInput(attrs={"aria-labelledby": "label_email"}),
            ),
            "zipcode": ZipCodeField(
                label="CEP de atendimento",
                mask="00000-000",
                widget=forms.TextInput(attrs={"aria-labelledby": "label_zipcode"}),
            ),
            "state": SelectField(
                choices=STATE_CHOICES,
                label="Estado",
                widget=forms.Select(attrs={"aria-labelledby": "label_state"}),
            ),
            "city": CharField(
                label="Cidade",
                required=False,
                widget=forms.Select(
                    attrs={"aria-labelledby": "label_city"},
                ),
            ),
            "neighborhood": CharField(
                label="Bairro",
                widget=forms.TextInput(attrs={"aria-labelledby": "label_neighborhood"}),
            ),
            "street": CharField(
                label="",
                required=False,
                widget=forms.TextInput(attrs={"style": "display:none"}),
            ),
            "lat": CharField(
                label="",
                required=False,
                widget=forms.TextInput(attrs={"style": "display:none"}),
            ),
            "lng": CharField(
                label="",
                required=False,
                widget=forms.TextInput(attrs={"style": "display:none"}),
            ),
        },
    },
    2: {
        "title": "Seus Dados",
        "subtitle": "",
        "fields": {
            "color": SelectField(
                label="Cor",
                choices=COLOR_CHOICES,
                widget=forms.Select(attrs={"aria-labelledby": "label_color"}),
            ),
            "gender": SelectField(
                label="Identidade de gênero",
                choices=GENDER_CHOICES,
                help_text="Mulher cisgênero: mulher que se identifica com o gênero que lhe foi atribuído o nascer. Mulher transgênero e travesti: mulher que se identifica com um gênero diferente daquele que lhe foi atribuído ao nascer.",
                widget=forms.Select(attrs={"aria-labelledby": "label_gender"}),
            ),
            "phone": MaskField(
                label="Whatsapp para contato",
                mask="(00) 0 0000-0000",
                min_length=14,
                help_text="Número de Whatsapp que utilizará para atendimento e contato com a equipe",
                error_messages={"min_length": "Por favor, insira o número completo."},
                widget=forms.TextInput(attrs={"aria-labelledby": "label_phone"}),
            ),
            "birth_date": DateField(
                label="Data de nascimento",
                widget=forms.DateInput(attrs={"aria-labelledby": "label_birth_date"}),
            ),
        },
    },
    3: {
        "title": "Disponibilidade",
        "subtitle": "Como voluntária, você se dispõe a atender pelo menos 1 mulher que precisa de ajuda com o mínimo de 1h de dedicação semanal. Se tiver disponibilidade, pode atender mais mulheres informando-nos abaixo:",
        "fields": {
            "availability": SelectField(
                label="Vagas para atendimento:",
                choices=AVAILABILITY_CHOICES,
                widget=forms.Select(attrs={"aria-labelledby": "label_availability"}),
            ),
            "modality": SelectField(
                label="Modalidade de atendimento",
                choices=MODALITY_CHOICES,
                widget=forms.Select(attrs={"aria-labelledby": "label_modality"}),
            ),
            "libras": SelectField(
                label="Atende em linguagem de sinais (libras)",
                choices=LIBRAS_CHOICE,
                widget=forms.Select(attrs={"aria-labelledby": "label_libras"}),
            ),
        },
    },
    4: {
        "title": "Experiência",
        "subtitle": "Há quanto tempo você atua com acolhimento de mulheres em situação de violência?",
        "fields": {
            "years_of_experience": ChoiceField(
                label="",
                widget=forms.RadioSelect,
                choices=YEARS_OF_EXPERIENCE_CHOICES,
            )
        },
    },
    5: {
        "title": "Campo de atuação",
        "subtitle": "",
        "fields": {},
    },
    6: {
        "title": "Abordagem",
        "subtitle": "",
        "fields": {
            "approach": ChoiceField(
                label="",
                widget=forms.RadioSelect,
                choices=APPROACH_CHOICES,
            )
        },
    },
    7: {
        "title": "Termo do Voluntariado",
        "subtitle": "A seguir, apresentaremos nosso Termo de Voluntariado e Diretrizes da organização. Leia atentamente e aceite todas as quatro etapas para seguir com o cadastro:",
        "fields": {"term_intro": CustomLogicField(label="", required=False)},
    },
    8: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_1": ChoiceField(
                label="Term 1", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
    9: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_2": ChoiceField(
                label="Term 2", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
    10: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_3": ChoiceField(
                label="Term 3", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
    11: {
        "title": "Termo do Voluntariado",
        "subtitle": "",
        "fields": {
            "term_4": ChoiceField(
                label="Term 4", widget=forms.HiddenInput, choices=TERM_CHOICES
            )
        },
    },
}


def current_step(step, type_form):
    if step in [1, 3, 4]:
        return form_steps.get(step)
    if step == 2:
        if type_form == "psicologa":
            form_step_2 = form_steps.get(step)
            form_step_2["fields"]["document_number"] = MaskField(
                label="CRP",
                mask="00/000000",
                min_length=5,
                error_messages={"min_length": "Por favor, insira o CRP completo."},
            )
        elif type_form == "advogada":
            form_step_2 = form_steps.get(step)
            form_step_2["fields"]["document_number"] = MaskField(
                label="OAB", mask="000000"
            )
        return form_step_2
    elif step == 5:
        form_step_5 = form_steps.get(step)
        if type_form == "advogada":
            form_step_5["fields"]["fields_of_work"] = forms.MultipleChoiceField(
                label="",
                widget=forms.CheckboxSelectMultiple,
                choices=FOW_LAWYER_CHOICES,
            )
        elif type_form == "psicologa":
            form_step_5["fields"]["fields_of_work"] = forms.MultipleChoiceField(
                label="",
                widget=forms.CheckboxSelectMultiple,
                choices=FOW_THERAPIST_CHOICES,
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
    return render(request=request, template_name="volunteers/home.html")


def fill_step(request, type_form, step):

    # caso esteja logada
    if request.user.is_authenticated:
        form_data = FormData.objects.get(user=request.user)

        total = form_data.total_steps

        if form_data.type_form != type_form:
            messages.success(
                request,
                "Você já preecheu o formulário como " + form_data.type_form + ".",
            )
            return HttpResponseRedirect("/")

        # se já finalizou mostra o modal da capacitação se foi aprovada cc volta pra home
        if form_data.step == total:
            if (
                "status" in form_data.values
                and form_data.values["status"] == "cadastrada"
            ):
                return render(
                    request,
                    "volunteers/home.html",
                    context={
                        "modal": True,
                        "moodle_url": f"{settings.MOODLE_API_URL}/login/index.php",
                    },
                )
            else:
                messages.success(
                    request,
                    "Você já preecheu o formulário com o email "
                    + form_data.values["email"].lower()
                    + ".",
                )
                return HttpResponseRedirect("/")

        # se estiver acessando um passo superior ao seu próximo passo redireciona para o  próximo passo
        if step > form_data.step + 1:
            if total == form_data.step:
                return HttpResponseRedirect(f"/{type_form}/final/")

            return HttpResponseRedirect(f"/{type_form}/{form_data.step+1}")

    elif step != 1:
        # se não estiver logada só pode acessar o primeiro passo
        return HttpResponseRedirect(f"/{type_form}/1")

    # pega o form do passo acessado
    step_form = current_step(step, type_form)

    if not step_form:
        raise Exception("Etapa não existe")

    fields = step_form["fields"]

    if request.method == "POST":
        form = VolunteerForm(fields=fields, data=request.POST)

        if form.is_valid():
            if step == 1:
                padrozined_email = form.cleaned_data["email"].lower()
                user, created = User.objects.get_or_create(username=padrozined_email)

                login(request, user)
                # manter usuario logado navegador
                request.session.set_expiry(0)

                form_data, created_form = FormData.objects.get_or_create(user=user)
                total = form_data.total_steps
                if created_form:
                    user.username = padrozined_email
                    user.first_name = form.cleaned_data["first_name"]
                    user.last_name = form.cleaned_data["last_name"]
                    user.email = padrozined_email
                    user.is_staff = False
                    user.save()
                    form_data.type_form = type_form
                    form_data.save()
                else:
                    if form_data.type_form != type_form:
                        messages.success(
                            request,
                            "Você já preecheu o formulário como "
                            + form_data.type_form
                            + ".",
                        )
                        return HttpResponseRedirect("/")

                    if form_data.step >= total - 1:
                        return HttpResponseRedirect(f"/{type_form}/final/")

                    # redireciona para passo após que parou
                    return HttpResponseRedirect(f"/{type_form}/{form_data.step+1}")

            else:
                # TODO se o passo não for 1 e não tiver usuario
                form_data = request.user.form_data

            form_data.step = step

            # TODO generalizar para todo tipo data?
            if "birth_date" in form.cleaned_data:
                form.cleaned_data["birth_date"] = str(form.cleaned_data["birth_date"])

            form_data.values = {**form_data.values, **form.cleaned_data}
            form_data.save()

            if step + 1 == total:
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

    return render(request, "volunteers/forms/step.html", context)


def final_step(request, type_form):
    # se não estiver logada direciona para o passo 1
    if not request.user.is_authenticated:
        return HttpResponseRedirect(f"/{type_form}/1")

    form_data = FormData.objects.get(user=request.user)
    total = form_data.total_steps
    context = dict(step=total, form=request.user.form_data)

    if (
        form_data.values["term_1"] == "Aceito"
        and form_data.values["term_2"] == "Aceito"
        and form_data.values["term_3"] == "Aceito"
        and form_data.values["term_4"] == "Aceito"
    ):
        form_data.values["status"] = "cadastrada"
    else:
        form_data.values["status"] = "reprovada_diretrizes_do_mapa"

    # se estiver ainda falta mais passos para finalizar o cadastro redireciona para o próximo passo
    if form_data.step < total - 1:
        return HttpResponseRedirect(f"/{type_form}/{form_data.step+1}")

    # se já finalizou mostra o modal da capacitação se foi aprovada cc volta pra home
    if form_data.step == total:
        if "status" in form_data.values and form_data.values["status"] == "cadastrada":
            return render(
                request,
                "volunteers/home.html",
                context={
                    "modal": True,
                    "moodle_url": f"{settings.MOODLE_API_URL}/login/index.php",
                },
            )
        else:
            messages.success(
                request,
                "Você já preecheu o formulário com o email "
                + form_data.values["email"]
                + ".",
            )
            return HttpResponseRedirect("/")

    if request.method == "POST":

        # se a voluntaria não aceitou os termos
        if form_data.values["status"] == "reprovada_diretrizes_do_mapa":
            return render(request, "volunteers/forms/failed-final-step.html", context)

        form_data.step = total
        form_data.save()

        # cria ou atualiza as tabelas volunteer e volunteer_availability
        volunteer = create_or_update_volunteer(form_data)

        # Zendesk
        zendesk_user_id = create_zendesk_user(
            form_data.values, form_data.type_form, volunteer.condition, volunteer.id
        )

        if zendesk_user_id:
            volunteer.zendesk_user_id = zendesk_user_id
            volunteer.save()
            if volunteer.condition == "cadastrada": 
                create_zendesk_ticket(volunteer, type_form)

        # se a voluntaria for reprovada
        if volunteer.condition in REJECTED_VOLUNTEERS:
            return render(request, "volunteers/forms/failed-final-step.html", context)

        # se ainda não foi cadastrada na capacitação
        if volunteer.moodle_id is None:
            moodle_info = create_and_enroll(
                form_data, form_data.values["city"], volunteer_id=volunteer.id
            )

            if "id" in moodle_info:
                volunteer.moodle_id = moodle_info["id"]
                volunteer.save()

            # send email
            send_welcome_email(volunteer.email, volunteer.first_name)

            if "password" in moodle_info:
                context["moodle_password"] = moodle_info["password"]

        # mostra modal para seguir para a capacitação
        context["modal"] = True
        context["moodle_url"] = f"{settings.MOODLE_API_URL}/login/index.php"

    return render(request, "volunteers/forms/final-step.html", context)


def address(request):
    try:
        zipcode = request.GET.get("zipcode")
        city = request.GET.get("city")
        state = request.GET.get("state")

        if zipcode:
            address = get_address_via_pycep(zipcode)

            if not address:
                address = get_address_via_brasil_api(zipcode)
        elif city and state:
            address = {"state": state, "city": city}
            address["neighborhood"] = request.GET.get("neighborhood")
            if "neighborhood" not in address:
                address["neighborhood"] = ""
        if address:

            formatCity = (
                unicodedata.normalize("NFD", unidecode(address["city"]))
                .replace("'", " ")
                .upper()
            )

            address["city"] = formatCity

            coordinates = get_coordinates_via_geocoding(address)
            if not coordinates:
                coordinates = get_coordinates_via_google_api(address)

            if not coordinates:
                coordinates = get_coordinates(address)

            address["coordinates"] = coordinates
            return JsonResponse(address)

    except KeyError as e:
        log_exception_details(e, request.GET, address)
        raise Http404()


def log_exception_details(exception, request_params, address):
    print(f"KeyError: {exception} occurred in the 'address' function.")
    print(f"Request GET parameters: {request_params}")
    print(f"Address dictionary: {address}")
    print("Keys in address dictionary:", address.keys())
    traceback.print_exc()
