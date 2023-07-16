from django.urls import path
from . import views


urlpatterns = [

    path("files/", views.RetrieveFilesView.as_view(), name="files"),
    path("files/<int:file_id>/<str:email>/email/", views.FileEmailAPIView.as_view(), name="email_sending"),
    path("files/<int:file_id>/download/", views.FileDownloadAPIView.as_view(), name="file_downloads")

]