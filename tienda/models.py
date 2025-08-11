from django.db import models
from datetime import date

class Producto(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    amount = models.IntegerField(verbose_name='Cantidad')
    created = models.DateField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateField(auto_now=True, verbose_name='Actualizado')
    image = models.ImageField(upload_to='imagenproducto')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
