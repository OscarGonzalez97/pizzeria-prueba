from django.db import models


class Pizza(models.Model):
    nombre = models.CharField('Nombre', max_length=250)
    precio = models.PositiveSmallIntegerField('Precio')
    activo = models.BooleanField('Activo', default=True)
    ingredientes = models.ManyToManyField('Ingrediente', related_name='ingredientes', verbose_name='Ingredientes')

    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):

    CATEGORIAS = (
        (10, 'Basico'),
        (20, 'Premium')
    )

    nombre = models.CharField('Nombre', max_length=250)
    categoria = models.PositiveSmallIntegerField('Categoria', choices=CATEGORIAS)

    def __str__(self):
        return self.nombre
