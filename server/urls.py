from django.urls import path
from . import views
from .views import email_sending_activity

urlpatterns = [

    path("files/", views.RetrieveFilesView.as_view(), name="files"),
    path("files/<int: file_id>/email/", email_sending_activity, name="email_sending")

]