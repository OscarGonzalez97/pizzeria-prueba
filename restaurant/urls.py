from django.urls import path, include

urlpatterns = [
    path('api/', include([
        path('auth/', include('auth_pizza.urls')),
    ]))]
