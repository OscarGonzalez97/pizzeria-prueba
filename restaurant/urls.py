from django.urls import path, include

from restaurant.views import PizzaListAPIView

urlpatterns = [
    path('api/', include([
        path('auth/', include('auth_pizza.urls')),
        path('pizzas/', PizzaListAPIView.as_view(), name='pizza-list'),
    ]))]
