from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwner

from ..models import Usuario
from ..serializers import UserSerializer

class Paginacao(PageNumberPagination):
    page_size = 3


class UserApiListViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    pagination_class = Paginacao
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsOwner(), ]
        return super().get_permissions()

