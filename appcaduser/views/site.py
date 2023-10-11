from django.shortcuts import render
from ..models import Usuario

def home(request):
    return render(request,'usuarios/home.html')


def usuarios(request):
    # Salvar os dados no banco
    usuario = Usuario()
    usuario.nome = request.POST.get('nome')
    usuario.sobrenome = request.POST.get('sobrenome')
    usuario.idade = request.POST.get('idade')
    usuario.save()

    #exibir os usuários cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #retornar os dados para a página
    return render(request,'usuarios/usuarios.html', usuarios)

