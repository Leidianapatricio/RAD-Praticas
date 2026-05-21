from django import forms
from .models import Autor, Livro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"