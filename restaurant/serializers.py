from rest_framework import serializers
from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    cantidad_ingredientes = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ('nombre', 'precio', 'cantidad_ingredientes')

    def get_cantidad_ingredientes(self, obj):
        return obj.ingredientes.count()
