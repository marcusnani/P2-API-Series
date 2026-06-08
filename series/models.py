from django.db import models

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    criador = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    temporadas = models.IntegerField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo