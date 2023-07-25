from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from allauth.account.views import confirm_email


urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
            confirm_email, name='account_confirm_email'),
    path('account-email-verification-sent/', views.AccountEmailVerificationSentView.as_view(),
         name='account_email_verification_sent'),
]
