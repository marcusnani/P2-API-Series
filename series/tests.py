from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Serie

class SerieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Serie.objects.create(
            titulo="Breaking Bad", 
            criador="Vince Gilligan", 
            ano_lancamento=2008, 
            temporadas=5, 
            genero="Drama"
        )

    def test_listar_series(self):
        response = self.client.get('/api/series/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)