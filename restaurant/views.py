from rest_framework import generics, permissions
from .models import Pizza, Ingrediente
from .serializers import PizzaSerializer, PizzaDetailSerializer, PizzaCreateSerializer, IngredienteSerializer


class PizzaListAPIView(generics.ListAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Pizza.objects.all()
        return Pizza.objects.filter(activo=True)


class PizzaDetailAPIView(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaDetailSerializer


class PizzaCreateAPIView(generics.CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaCreateSerializer
    permission_classes = [permissions.IsAdminUser]


class PizzaUpdateAPIView(generics.UpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaCreateSerializer
    permission_classes = [permissions.IsAdminUser]


class IngredienteListCreateView(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAdminUser]


class IngredienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAdminUser]
