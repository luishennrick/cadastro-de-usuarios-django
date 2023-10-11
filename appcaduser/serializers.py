from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Nome = serializers.CharField(source='nome')
    Sobrenome = serializers.CharField(source='sobrenome')
    idade = serializers.IntegerField()
    nomeCompleto = serializers.SerializerMethodField(
        method_name= 'nomeEsobrenome'
    )

    def nomeEsobrenome(self, usuario):
        return f'{usuario.nome} {usuario.sobrenome}'