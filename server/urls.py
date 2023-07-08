from django.urls import path
from . import views

urlpatterns = [

    path("files/", views.RetrieveFilesView.as_view(), name="files")

]