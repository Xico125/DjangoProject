from django.db import models

class AvaliacaoTreino(models.Model):
    nome = models.CharField(max_length=100)
    disponibilidade = models.IntegerField()
    intensidade = models.IntegerField()
    nota_geral = models.IntegerField()
    opiniao = models.TextField()

    def __str__(self):
        return f"{self.nome} - Nota {self.nota_geral}"
