from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import SignupSerializer, ResetPasswordSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.


class SignupView(GenericAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny, ]
    parser_classes = [JSONParser]

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Signup is succesful"
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message": "Signup unsuccessful, Username or email already exits"
        }

        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    permission_classes = [AllowAny, ]
    parser_classes = [JSONParser]

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            token, created = Token.objects.get_or_create(user=user)

            response = {
                "message": "Login successful",
                "token": token.key
            }

            return Response(data=response, status=status.HTTP_200_OK)

        response = {
            "message": "Login Failed"
        }

        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny,]
    parser_classes = [JSONParser]

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Password reset successful"
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
