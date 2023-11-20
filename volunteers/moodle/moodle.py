from volunteers.moodle import moodle_api
from django.conf import settings
from volunteers.models import IntegrationLogs


def create_and_enrol(form_data, city, volunteer_id):
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
        form_data=form_data,
        integration="moodle",
        type="criar",
        data=user,
        status="draft",
    )

    try:
        response = moodle_api.call("core_user_create_users", users=[user])
        log.external_data = response[0]["id"]
        log.status = "usuária criada"
        log.save()
    except Exception as err:
        log.error = err
        log.status = "erro"
        log.save()
        return False

    logEnrol = IntegrationLogs.objects.create(
        form_data=form_data,
        integration="moddle",
        type="matricular",
        data=user,
        status="draft",
    )
    try:
        moodle_api.call(
            "enrol_manual_enrol_users",
            enrolments=[{"roleid": 5, "userid": response[0]["id"], "courseid": 2}],
        )
        logEnrol.external_data = response[0]["id"]
        logEnrol.status = "usuária matriculada"
        logEnrol.save()
    except Exception as err:
        logEnrol.error = err
        logEnrol.status = "erro"
        logEnrol.save()
        return False

    return True
