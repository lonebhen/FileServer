from django.urls import path
from . import views
# from .views import email_sending_activity

urlpatterns = [

    path("files/", views.RetrieveFilesView.as_view(), name="files"),
    path("files/<int:file_id>/email/", views.FileEmailAPIView.as_view(), name="email_sending"),
    path("files/<int:file_id>/download/", views.FileDownloadAPIView.as_view(), name="file_downloads")

]