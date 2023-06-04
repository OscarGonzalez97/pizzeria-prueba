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


class PizzaCreateSerializer(serializers.ModelSerializer):
    ingredientes = serializers.PrimaryKeyRelatedField(
        queryset=Ingrediente.objects.all(),
        many=True
    )

    class Meta:
        model = Pizza
        fields = ('nombre', 'precio', 'activo', 'ingredientes')

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.activo = validated_data.get('activo', instance.activo)

        # Actualizar los ingredientes de la pizza
        ingredientes = validated_data.get('ingredientes')
        if ingredientes is not None:
            instance.ingredientes.set(ingredientes)

        instance.save()
        return instance
