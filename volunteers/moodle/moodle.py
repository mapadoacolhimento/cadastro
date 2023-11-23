from volunteers.moodle import moodle_api
from django.conf import settings
from volunteers.models import IntegrationLogs


def create_and_enroll(form_data, city, volunteer_id):
    moodle_api.URL = settings.MOODLE_API_URL
    moodle_api.KEY = settings.MOODLE_API_KEY

    if form_data.type_form == "psicologa":
        ocuppation = "Psicóloga"
    else:
        ocuppation = "Advogada"

    user = {
        "firstname": form_data.values["first_name"],
        "lastname": form_data.values["last_name"],
        "email": form_data.values["email"],
        "username": form_data.values["email"],
        "city": city,
        "customfields": [
            {"type": "occupation", "value": ocuppation},
            {"type": "volunteer_id", "value": volunteer_id},
        ],
        "auth": "manual",
        "createpassword": 1,
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

    # TODO esttegia quando a mtricula não for realizada

    return response[0]["id"]
