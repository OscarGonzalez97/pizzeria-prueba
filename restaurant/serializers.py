from rest_framework import serializers
from .models import Pizza, Ingrediente


class PizzaSerializer(serializers.ModelSerializer):
    cantidad_ingredientes = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ('nombre', 'precio', 'cantidad_ingredientes')

    def get_cantidad_ingredientes(self, obj):
        return obj.ingredientes.count()


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('nombre', 'categoria')


class PizzaDetailSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ('nombre', 'precio', 'activo', 'ingredientes')
