from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CadastroUsuarioForm(UserCreationForm):

    username = forms.CharField(
        label="Usuário",
        help_text="",
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Digite seu usuário",
            "autocomplete": "off"
        })
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Digite seu email",
            "autocomplete": "off"
        })
    )

    password1 = forms.CharField(
        label="Senha",
        help_text="",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Digite sua senha",
            "autocomplete": "new-password"
        })
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        help_text="",
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Confirme sua senha",
            "autocomplete": "new-password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]