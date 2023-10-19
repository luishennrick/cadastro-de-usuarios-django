from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from ..models import Usuario
from ..serializers import UserSerializer


class UserApiList(APIView):
    def get(self, request):
        usuario = Usuario.objects
        serializer = UserSerializer(instance=usuario, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApiListDetail(APIView):
    def get_user(self, pk):
        usuario = get_object_or_404(
            Usuario.objects,
            pk=pk
        )
        return usuario
    
    def get(self, request, pk):
            usuario = self.get_user(pk)
            serializer = UserSerializer(instance=usuario, many=False)
            return Response(serializer.data)

    def patch(self, request, pk):
            usuario = self.get_user(pk)
            serializer = UserSerializer(
                instance=usuario, data=request.data, 
                many=False, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
            usuario = self.get_user(pk)
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    