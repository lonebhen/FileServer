from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Files, FileActivity
from .serializers import FileSerializer, FileActivitySerializer


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

@api_view(['POST'])
def email_sending_activity(request: Request, file_id: int):
    try:
        file = Files.objects.get(pk = file_id)
        file_activity = file.fileactivity

        file_activity.emailed += 1
        file_activity.save()

        response = {
            "message": "File sent succesful"
        }

        return Response(data=response, status=status.HTTP_200_OK)
    
    except Files.DoesNotExist:
        response = {
            "message": "File does not exist"
        }

        return Response(data=response, status=status.HTTP_404_NOT_FOUND)