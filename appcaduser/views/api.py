from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404

from ..models import Usuario
from ..serializers import UserSerializer


class UserApiList(ListCreateAPIView):
    queryset = Usuario.objects
    serializer_class = UserSerializer

class UserApiListDetail(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects
    serializer_class = UserSerializer

