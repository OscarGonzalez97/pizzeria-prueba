from django.urls import path, include

from restaurant.views import PizzaListAPIView, PizzaDetailAPIView, PizzaCreateAPIView, PizzaUpdateAPIView, \
    IngredienteListCreateView, IngredienteRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', include([
        path('auth/', include('auth_pizza.urls')),
        # pizzas
        path('pizzas/', PizzaListAPIView.as_view(), name='pizza-list'),
        path('pizzas/create', PizzaCreateAPIView.as_view(), name='pizza-create'),
        path('pizzas/update/<int:pk>', PizzaUpdateAPIView.as_view(), name='pizza-update'),
        path('pizzas/<int:pk>/', PizzaDetailAPIView.as_view(), name='pizza-detail'),
        # ingredientes
        path('ingredientes/', IngredienteListCreateView.as_view(), name='ingredient-list-create'),
        path('ingredientes/<int:pk>/', IngredienteRetrieveUpdateDestroyView.as_view(),
             name='ingredient-retrieve-update-destroy'),
    ]))]
