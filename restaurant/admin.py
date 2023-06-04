from django.contrib import admin
from .models import Pizza, Ingrediente


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
