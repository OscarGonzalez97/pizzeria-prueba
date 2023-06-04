from django.urls import path, include

from restaurant.views import PizzaListAPIView, PizzaDetailAPIView

urlpatterns = [
    path('api/', include([
        path('auth/', include('auth_pizza.urls')),
        path('pizzas/', PizzaListAPIView.as_view(), name='pizza-list'),
        path('pizzas/<int:pk>/', PizzaDetailAPIView.as_view(), name='pizza-detail'),
    ]))]
