from rest_framework import generics
from .models import Pizza
from .serializers import PizzaSerializer, PizzaDetailSerializer


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