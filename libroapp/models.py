from django.db import models
from django.utils import timezone

class Libro(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"