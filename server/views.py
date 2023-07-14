from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Files
from .serializers import FileSerializer


# Create your views here.


class RetrieveFilesView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer


    def get(self, request: Request):
        files = Files.objects.all()

        seriaizer = self.serializer_class(instance=files, many = True)

        response = {
            "message": "These are al the files",
            "data": seriaizer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)


class FileEmailAPIView(APIView):
    def post(self, request: Request, file_id: int, email: str):
        try:
            file = Files.objects.get(id=file_id)
            
            file.number_of_emails += 1
            file.save()

            return Response({"message": "File emailed count updated."})
        except Files.DoesNotExist:
            return Response({"message": "File not found."})
        
class FileDownloadAPIView(APIView):
    def post(self, request: Request, file_id: int):
        try:
            file = Files.objects.get(id=file_id)
            
            file.number_of_downloads += 1
            file.save()

            return Response({"message": "File download count updated."})
        except Files.DoesNotExist:
            return Response({"message": "File not found."})