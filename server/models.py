import os
from django.db import models
import uuid
from django.utils.deconstruct import deconstructible



@deconstructible
class upload_to(object):
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        filename = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        return f"uploads/{self.sub_path}/{filename}"



class Files(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    file = models.FileField(upload_to= upload_to('files'))

    number_of_emails = models.PositiveIntegerField(default=0)
    number_of_downloads = models.PositiveIntegerField(default=0)



    class Meta:
        verbose_name_plural = "Files"


    def __str__(self) -> str:
        return self.name
    



