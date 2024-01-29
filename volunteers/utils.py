from django.conf import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To


def send_welcome_email(email, name):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    from_email = From(settings.DEFAULT_FROM_EMAIL, "Equipe do Mapa do Acolhimento")
    to_email = To(email, name)
    message = Mail(
        from_email,
        to_email,
    )
    message.dynamic_template_data = {"name": name, "email": email}
    message.template_id = "d-fdc7b14cee8847f79625af3bb8b37efd"
    response = sg.send(message)
    return response
