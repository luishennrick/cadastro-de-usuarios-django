from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from ..models import Usuario
from ..serializers import UserSerializer

@api_view(http_method_names=['get', 'post'])
def user_api_list(request):
    if request.method == 'GET':
        usuario = Usuario.objects
        serializer = UserSerializer(instance=usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(http_method_names=['get', 'patch', 'delete'])
def user_api_detail(request, pk):
    usuario = Usuario.objects.filter(pk=pk).first()
    if usuario:
        if request.method == 'GET':
            serializer = UserSerializer(instance=usuario, many=False)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = UserSerializer(
                instance=usuario, data=request.data, 
                many=False, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response({
            'detail': 'Usuário não encontrado'
        }, status=status.HTTP_404_NOT_FOUND)