from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from decimal import Decimal

from edu.models import Livro, Editora


class Command(BaseCommand):
    help = "Gera 100 livros usando Faker"

    def handle(self, *args, **kwargs):
        fake = Faker("pt_BR")

        editora, _ = Editora.objects.get_or_create(nome="Editora Faker")

        for i in range(100):
            Livro.objects.create(
                isbn=fake.isbn13(separator="")[:13],
                titulo=fake.sentence(nb_words=4),
                publicacao=fake.date_between(start_date="-20y", end_date="today"),
                preco=Decimal(randint(20, 200)),
                estoque=randint(1, 100),
                editora=editora
            )

        self.stdout.write(
            self.style.SUCCESS("100 livros gerados com sucesso!")
        )