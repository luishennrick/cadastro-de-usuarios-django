from django.test import TestCase
from .models import Usuario
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome="John",
            sobrenome="Doe",
            idade=30
        )

    def test_nome_sobrenome(self):
        self.assertEqual(self.usuario.nome, "John")
        self.assertEqual(self.usuario.sobrenome, "Doe")

    def test_idade(self):
        self.assertEqual(self.usuario.idade, 30)

class UserApiListViewSetTestCase(APITestCase):
    def setUp(self):

        # Crie alguns objetos Usuario relacionados aos usuários
        self.usuario1 = Usuario.objects.create(nome='John', sobrenome='Doe', idade=30)
        self.usuario2 = Usuario.objects.create(nome='Jane', sobrenome='Smith', idade=25)
        self.usuario3 = Usuario.objects.create(nome='Bob', sobrenome='Johnson', idade=35)

    def test_pagination(self):
        # Faça uma solicitação GET para a lista de usuários com paginação
        url = reverse('user-api-list')
        response = self.client.get(url)
        
        # Verifique se a resposta está OK (status 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifique se o número correto de itens está sendo retornado de acordo com a páginação
        self.assertEqual(len(response.data['results']), 3)  # page_size definido como 3