from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.register_user, name='register'),
    path('enviar-codigo/', views.send_verification_code, name='enviar_codigo'),
    path('verificacao-de-codigo/', views.confirm_code, name='verificacao_de_codigo'),
]