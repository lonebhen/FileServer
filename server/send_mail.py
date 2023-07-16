import os
import mimetypes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from .models import Files
from storages.backends.s3boto3 import S3Boto3Storage

def send_file_email(id: int, email: str):
    file_object = get_object_or_404(Files, pk=id)
    file_name = file_object.name

    email_subject = "File From Fileserver"
    email_body = "File you requested from fileserver app"
    email_from = "ben.angmortey@gmail.com"
    email_to = email

    email = MIMEMultipart()
    email["Subject"] = email_subject
    email["From"] = email_from
    email["To"] = email_to

    # Retrieve file data from Amazon S3
    file_path = file_object.file.name
    storage = S3Boto3Storage()
    file_data = storage.open(file_path, "rb").read()

    # Attach the file to the email
    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None or encoding is not None:
        content_type = "application/octet-stream"

    maintype, subtype = content_type.split("/", 1)
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(file_data)
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=file_name)
    email.attach(attachment)


    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login("ben.angmortey@gmail.com", "uuyhmqzqikfimosg")
        server.sendmail(email_from, email_to, email.as_string())
