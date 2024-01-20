from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'idade', 'nomeCompleto']

    nomeCompleto = serializers.SerializerMethodField(
        method_name = 'nomeEsobrenome'
    )       

    def nomeEsobrenome(self, usuario):
        return f'{usuario.nome} {usuario.sobrenome}'