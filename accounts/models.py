from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.


class CustomUser(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_active") is not True:
            raise ValueError(
                "Admin must have the is_active attribute set to true")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Admin must have is_active attribute set to True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Admin must have is_active attribute set to True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(max_length=50)

    objects = CustomUser()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f"{self.username} -> {self.email}"
