from django.conf import settings
import secrets
from string import ascii_letters, digits

from volunteers.models import IntegrationLogs
from volunteers.moodle import moodle_api
from volunteers.moodle.models import MdlUserPreferences


def create_password(length):
    symbols = "!#$%&()*+><^~@-_`/|¿"
    alphabet = ascii_letters + digits + symbols

    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        if (
            any(
                (c.islower() and c not in symbols) for c in password
            )  # tem alguma letra minúscula
            and any(
                (c.isupper() and c not in symbols) for c in password
            )  # tem alguma letra maiúscula
            and any(c in symbols for c in password)  # tem algum símbolo
            and any(c.isdigit() for c in password)
        ):  # tem pelo menos 1 dígitos
            break  # deu certo, sai do while

    return password


def create_and_enroll(form_data, city, volunteer_id):
    moodle_api.URL = settings.MOODLE_API_URL
    moodle_api.KEY = settings.MOODLE_API_KEY

    if form_data.type_form == "psicologa":
        occupation = "Psicóloga"
    else:
        occupation = "Advogada"

    password = create_password(8)

    user = {
        "firstname": form_data.values["first_name"],
        "lastname": form_data.values["last_name"],
        "email": form_data.values["email"].lower(),
        "username": form_data.values["email"].lower(),
        "city": city,
        "customfields": [
            {"type": "occupation", "value": occupation},
            {"type": "volunteer_id", "value": volunteer_id},
        ],
        "auth": "manual",
        "password": password,
    }

    log = IntegrationLogs.objects.create(
        integration="moodle",
        internal_id=volunteer_id,
        type="criar",
        data=user,
        status="draft",
        form_type=form_data.type_form,
    )

    try:
        response = moodle_api.call("core_user_create_users", users=[user])
        log.external_id = response[0]["id"]

        log.status = "usuária criada"
        log.save()

        MdlUserPreferences.objects.create(
            userid=log.external_id, name="auth_forcepasswordchange", value=1
        )

    except Exception as err:
        # TODO se já existir no moodle buscar o id e verificar matricula

        log.error = err
        log.status = "erro"
        log.save()
        return

    logEnrol = IntegrationLogs.objects.create(
        integration="moodle",
        internal_id=volunteer_id,
        type="matricular",
        data=user,
        status="draft",
        form_type=form_data.type_form,
    )
    try:
        moodle_api.call(
            "enrol_manual_enrol_users",
            enrolments=[{"roleid": 5, "userid": response[0]["id"], "courseid": 2}],
        )
        logEnrol.external_id = response[0]["id"]

        logEnrol.status = "usuária matriculada"
        logEnrol.save()
    except Exception as err:
        logEnrol.error = err
        logEnrol.status = "erro"
        logEnrol.save()

    # TODO esttegia quando a matricula não for realizada

    return {"id": response[0]["id"], "password": password}
