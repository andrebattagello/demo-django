# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from lista.models import Lista


class VerListaSpec(TestCase):

    def setUp(self):
        self.client = Client()

    def deve_saber_mostrar_lista_vazia(self):
        Lista()
        response = self.client.post('/lista/')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Lista Vazia')
