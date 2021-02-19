from celery.utils.log import get_task_logger
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from project.celery import app

logger = get_task_logger(__name__)



@app.task(name="email_contact", serializer='pickle')  # <- change instead JSON serializer
def email_contact(message):
    try:
        logger.info('Starting email_contact..')
        subject: str = f' --> Hi a new subject'
        from_email: str = EMAIL_HOST_USER
        to: str = EMAIL_TO

        with open(BASE_DIR + "/templates/mail/contact.html") as html: # <- create a default template email
            contact_message = html.read()
        message = EmailMultiAlternatives(subject=subject, to=[to], from_email=from_email, body=contact_message)
        html_message = get_template("mail/contact.html") \
            .render({'args': *args})  # <- Args to pass inside in template
        message.attach_alternative(html_message, "text/html")
        message.send()
        logger.info('Finninsh email_contact..')

    except Exception as error:
        logger.info(error)
        raise error