from django.shortcuts import render, redirect
from .forms import RegistroForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})
