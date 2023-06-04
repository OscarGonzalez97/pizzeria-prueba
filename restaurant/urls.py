from django.urls import path, include

from restaurant.views import PizzaListAPIView, PizzaDetailAPIView, PizzaCreateAPIView, PizzaUpdateAPIView

urlpatterns = [
    path('api/', include([
        path('auth/', include('auth_pizza.urls')),
        path('pizzas/', PizzaListAPIView.as_view(), name='pizza-list'),
        path('pizzas-create/', PizzaCreateAPIView.as_view(), name='pizza-create'),
        path('pizzas-update/<int:pk>', PizzaUpdateAPIView.as_view(), name='pizza-create'),
        path('pizzas/<int:pk>/', PizzaDetailAPIView.as_view(), name='pizza-detail'),
    ]))]
