from rest_framework import serializers
from .models import Files



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ["id", "name", "description", "file"]


# class FileActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FileActivity
#         fields = "__all__"