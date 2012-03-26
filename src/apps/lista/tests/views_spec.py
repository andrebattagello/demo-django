# -*- coding: utf-8 -*-
from django.test import TestCase
#from django.test import Client
from django.test.client import RequestFactory
# I usually use assert_equals instead of plain assert
# to have a comparison between expected and real on assertion error
from nose.tools import assert_equals
from factories import cria_lista_nao_vazia, cria_lista_vazia
from lista import views


class VerListaSpec(TestCase):  # Specification
    """
    Comportamento da view ver_lista
    """
    def setUp(self):
        self.request = RequestFactory().get('/lista/')
        #self.client = Client()

    def deve_saber_mostrar_lista_vazia(self):
        cria_lista_vazia()
        response = views.ver_lista(self.request)
        assert_equals(response.status_code, 200)
        assert_equals(response.template_name, 'lista/ver_lista.html')
        assert_equals(len(response.context_data['lista']), 0)

    def deve_saber_mostrar_lista_com_items(self):
        lista = cria_lista_nao_vazia()
        response = views.ver_lista(self.request)
        assert_equals(response.status_code, 200)
        assert_equals(response.template_name, 'lista/ver_lista.html')
        assert len(response.context_data['lista']) > 0
        for item in lista.itens.all():
            assert item in response.context_data['lista']
