from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "https://fileserver-six.vercel.app/reset-password?token={}".format(reset_password_token.key)
    }

    email_html_message = render_to_string(
        'account/email/user_reset_password.html', context)
    email_plaintext_message = render_to_string(
        'account/email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="File Server App"),
        # message:
        email_plaintext_message,
        # from:
        "ben.angmortey@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


class AccountEmailVerificationSentView(APIView):
    def get(self, request):
        return Response({'message': 'Account email verification sent.'})
