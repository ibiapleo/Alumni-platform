from django.shortcuts import render, redirect
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/criar_tarefa.html')
