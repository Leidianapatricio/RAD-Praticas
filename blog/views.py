from django.shortcuts import render
from datetime import datetime


def home(request):
    contexto = {
        "nome": "Leidiana",
        "data": datetime.now(),
        "is_logged_in": True,
        "role": "admin",
        "produtos": [
            {"nome": "Notebook", "preco": 3000},
            {"nome": "Mouse", "preco": 100},
            {"nome": "Teclado", "preco": 200},
        ]
    }
    return render(request, "blog/home.html", contexto)

def contato(request, telefone):
    return render(request, "blog/contato.html", {"telefone": telefone})





