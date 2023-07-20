from django.shortcuts import render
from django.http import FileResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Files
from .serializers import FileSerializer
from .send_mail import send_file_email


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
            send_file_email(file_id, email)
            file = Files.objects.get(id=file_id)
            
            file.number_of_emails += 1
            file.save()

            return Response({"message": "File emailed and count updated."})
        except Files.DoesNotExist:
            return Response({"message": "File not found."})
        
class FileDownloadAPIView(APIView):
    def post(self, request: Request, file_id: int):
        try:
            file = Files.objects.get(id=file_id)
            
            file.number_of_downloads += 1
            file.save()

            response = FileResponse(file.file, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file.name}"'
            return response


        except Files.DoesNotExist:
            return Response({"message": "File not found."})