from django.shortcuts import render, redirect
from .forms import RegistroForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  
            user.save()
            return redirect('login') 
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})