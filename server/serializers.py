from rest_framework import serializers
from .models import Files, FileActivity



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"


class FileActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileActivity
        fields = "__all__"