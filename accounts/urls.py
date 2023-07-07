from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("pass-reset/", views.ResetPasswordView.as_view(), name="password_reset")
]
