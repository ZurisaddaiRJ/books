from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.
class Libro(models.Model):
    titulo = models.TextField (default='',blank=False)
    autor = models.TextField (default='',blank=False)
    genero = models.TextField (default='',blank=False)
    editorial = models.TextField (default='',blank=False)
    anio = models.IntegerField(default = 0,blank=False)
    num_pages = models.IntegerField(default=0,blank=False)
    costo = models.DecimalField(default=0, max_digits=5, decimal_places=2,blank=False)
    categoria = models.TextField (default=' ', blank=False)
    edicion = models.IntegerField(default=0,blank=False)
    idioma = models.TextField(default=' ', blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('libros.Libro', related_name='books', on_delete=models.CASCADE)

