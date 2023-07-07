from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email_exits = User.objects.filter(email=attrs["email"]).exists()
        username_exits = User.objects.filter(
            username=attrs["username"]).exists()

        if email_exits or username_exits:
            raise ValidationError("User with this account exits")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)

        user.set_password(password)
        Token.objects.create(user=user)
        user.save()

        return user


class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    new_password = serializers.CharField(min_length=8, write_only=True)

    def validate_username(self, username):
        user = User.objects.filter(username=username).exists()

        if user is None:
            raise ValidationError("This username does not exit")
        return username

    def save(self):
        user = User.objects.get(username=self.validated_data["username"])
        user.set_password(self.validated_data["new_password"])
        user.save()
