from rest_framework import serializers
from .models import Autor, Editora


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"