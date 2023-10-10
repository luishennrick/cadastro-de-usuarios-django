from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()