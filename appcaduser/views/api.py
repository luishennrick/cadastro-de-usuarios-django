from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from ..models import Usuario
from ..serializers import UserSerializer

class Paginacao(PageNumberPagination):
    page_size = 3


class UserApiListViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    pagination_class = Paginacao


