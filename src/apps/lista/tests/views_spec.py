# -*- coding: utf-8 -*-
from django.test import TestCase
#from django.test import Client
from django.test.client import RequestFactory
# I usually use assert_equals instead of plain assert
# to have a comparison between expected and real on assertion error
from nose.tools import assert_equals
from factories import cria_lista_nao_vazia, cria_lista_vazia, cria_item
from lista import views
from lista.forms import ItemForm
from lista.models import Item


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
        for item in lista:
            assert item in response.context_data['lista']


class VerDetalhesItemSpec(TestCase):
    """
    Comportamento da view ver_detalhes_item
    """
    def setUp(self):
        self.item = cria_item()
        self.request = RequestFactory().get('/lista/%s/' % self.item.id)
        #self.client = Client()

    def deve_saber_apresentar_a_pagina_corretamente(self):
        response = views.ver_detalhes_item(self.request, self.item.id)
        assert_equals(response.status_code, 200)
        assert_equals(response.template_name, 'lista/ver_detalhes_item.html')
        assert_equals(response.context_data['form'].__class__, ItemForm)
        assert_equals(response.context_data['form'].instance, self.item)

    def deve_saber_mudar_o_estado_de_completo_de_um_item(self):
        assert self.item.completo is False

        # de incompleto para completo
        post_data = {'completo': 1, 'nome': self.item.nome}
        response = self.client.post('/lista/%s/' % self.item.id, post_data)
        assert_equals(response.status_code, 302)  # em POST o sucesso eh 302
        assert response['Location'].endswith('/lista/')  # verifica o Redirect
        # refresh da nossa instancia na memoria com as atualizacoes no DB
        self.item = Item.objects.get(id=self.item.id)
        assert self.item.completo is True

        # de completo para incompleto
        post_data['completo'] = 0
        response = self.client.post('/lista/%s/' % self.item.id, post_data)
        assert_equals(response.status_code, 302)  # em POST o sucesso eh 302
        assert response['Location'].endswith('/lista/')  # verifica o Redirect
        # refresh da nossa instancia na memoria com as atualizacoes no DB
        self.item = Item.objects.get(id=self.item.id)
        assert self.item.completo is False
