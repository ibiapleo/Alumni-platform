from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")
    email = forms.EmailField(max_length=254, required=True, label='Email válido')
    instituicao = forms.CharField(max_length=100, required=False, label="Instituição de Ensino")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'instituicao', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.profile.instituicao = self.cleaned_data['instituicao']
        if commit:
            user.save()
            user.profile.save()
        return user
