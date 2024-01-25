from django.conf import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_welcome_email(email, name):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=email,
    )
    message.dynamic_template_data = {"name": name, "email": email}
    message.template_id = "d-fdc7b14cee8847f79625af3bb8b37efd"
    response = sg.send(message)
    return response
