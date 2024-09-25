from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('enviar-codigo/', views.send_verification_code, name='enviar_codigo'),
    path('confirmar-codigo/', views.confirm_code, name='confirmar_codigo'),
    path('reenviar-codigo/', views.send_verification_code, name='reenviar_codigo'),
]