from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = "Welcome to Our Platform"
    message = "Thank you for signing up! We're excited to have you."
    from_email = "example123@gmail.com"  # Replace this with a verified sender
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return "Email Sent Successfully"
