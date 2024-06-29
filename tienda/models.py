from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    artista = models.CharField(max_length=70)
    album = models.CharField(max_length=70)
    precio = models.IntegerField()
    portada = models.ImageField(upload_to="productos", null=True)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return self.album