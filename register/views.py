from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.http import JsonResponse
import json

def register_user(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  
            user.save()
            return redirect('login') 
    else:
        form = RegistroForm()
    return render(request, 'register/registro.html', {'form': form})

def send_verification_code(request, user_email):
    code = get_random_string(length=6, allowed_chars='0123456789')
    
    request.session['verification_code'] = code
    
    send_mail(
        'Seu código de verificação',
        f'Por favor, use o seguinte código para verificar sua conta: {code}',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )
    
    return redirect('verificacao_de_codigo')

def confirm_code(request):
    if request.method == 'POST':
        code_entered = ''.join(request.POST.getlist('code'))
        code_sent = request.session.get('verification_code')
        data = json.loads(request.body)
        
        if code_entered == code_sent:
            messages.success(request, 'E-mail verificado com sucesso!')
            return JsonResponse({'success': True})
        else:
            messages.error(request, 'Código inválido. Tente novamente.')
            return JsonResponse({'success': False})
      
    
    return render(request, 'register/verificacao_de_codigo.html')


