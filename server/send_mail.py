from django.core.mail import send_mail, EmailMessage
from .models import Files
from django.shortcuts import get_object_or_404
import boto3
from botocore.exceptions import NoCredentialsError
from rest_framework.response import Response


def send_file_email(id: int, email: str):
    # file_object = get_object_or_404(Files, pk= id)

    # file = file_object.file

    # email_subject = "File From Fileserver"
    # email_body = "File you requested from fileserver app"

    # email_from = "ben.angmortey@gmail.com"

    # email_to = email

    # email = EmailMessage(email_subject, email_body, email_from, [email_to] )

    # try:
    #     s3_client = boto3.client('s3')
    #     response = s3_client.get_object(Bucket='ben-fileserver', Key=str(file))
    #     file_data = response['Body'].read()

    #     # Attach the file to the email
    #     email.attach(file.name, file_data, 'application/octet-stream')

    #     # Send the email
    #     email.send()

    # except NoCredentialsError:
    #     return Response({"message": "Failed to send email. Amazon S3 credentials not found."})

    # except Exception as e:
    #     return Response({"message": "Failed to send email. Error: " + str(e)})

    # # file_data = file.read()

    # # email.attach('filename.ext', file_data, 'application/octet-stream')

    # # email.send()


    file_object = get_object_or_404(Files, pk= id)

    file_name = file_object.name

    email_subject = "File From Fileserver"
    email_body = "File you requested from fileserver app"

    email_from = "ben.angmortey@gmail.com"

    email_to = email


    email = EmailMessage(email_subject, email_body, email_from, [email_to] )

    # send_mail(email_subject, email_body, email_from, [email_to],
    #           attachments=[(file_name, file_object.file, 'application/octet-stream')])


    file_content = file_object.file.read()
    email.attach(file_name, file_content, 'application/octet-stream')

    # Send the email
    email.send()

