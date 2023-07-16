from rest_framework import serializers
from .models import Files



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ["id", "name", "description", "file"]


