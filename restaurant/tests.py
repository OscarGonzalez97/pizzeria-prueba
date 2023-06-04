from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Pizza, Ingrediente
from auth_pizza.models import Usuario

class PizzaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create_user(email='testuser', username='testuser', password='testpassword', is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.pizza1 = Pizza.objects.create(nombre='Pizza 1', precio=10, activo=True)
        self.pizza2 = Pizza.objects.create(nombre='Pizza 2', precio=15, activo=False)
        self.ingrediente1 = Ingrediente.objects.create(nombre='Ingrediente 1', categoria=10)
        self.ingrediente2 = Ingrediente.objects.create(nombre='Ingrediente 2', categoria=20)

    def test_pizza_list_no_user(self):
        self.client.logout()
        url = reverse('pizza-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Solo se debe mostrar la pizza activa

    def test_pizza_list(self):
        url = reverse('pizza-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # debe mostrar todas

    def test_pizza_create_no_user(self):
        self.client.logout()
        url = reverse('pizza-create')
        data = {
            'nombre': 'Nueva Pizza',
            'precio': 20,
            'activo': True,
            'ingredientes': [self.ingrediente1.id, self.ingrediente2.id]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_pizza_create(self):
        url = reverse('pizza-create')
        data = {
            'nombre': 'Nueva Pizza',
            'precio': 20,
            'activo': True,
            'ingredientes': [self.ingrediente1.id, self.ingrediente2.id]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 3)

    def test_pizza_update(self):
        url = reverse('pizza-update', args=[self.pizza1.id])
        data = {
            'nombre': 'Pizza Actualizada',
            'precio': 12,
            'activo': True,
            'ingredientes': [self.ingrediente1.id]
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pizza.objects.get(id=self.pizza1.id).nombre, 'Pizza Actualizada')

    def test_pizza_detail(self):
        self.client.logout()
        url = reverse('pizza-detail', args=[self.pizza1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.pizza1.nombre)

    def test_ingrediente_list(self):
        url = reverse('ingredient-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_ingrediente_create(self):
        url = reverse('ingredient-list-create')
        data = {
            'nombre': 'Ingrediente',
            'categoria': 20,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingrediente.objects.count(), 3)

    def test_ingrediente_create_no_user(self):
        self.client.logout()
        url = reverse('ingredient-list-create')
        data = {
            'nombre': 'Ingrediente',
            'categoria': 20,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Ingrediente.objects.count(), 2)

    def test_ingrediente_retrieve_update_destroy(self):
        url = reverse('ingredient-retrieve-update-destroy', args=[self.ingrediente1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.ingrediente1.nombre)

        data = {
            'nombre': 'Ingrediente Actualizado',
            'categoria': 20
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ingrediente.objects.get(id=self.ingrediente1.id).nombre, 'Ingrediente Actualizado')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ingrediente.objects.count(), 1)


