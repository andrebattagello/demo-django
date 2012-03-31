# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import RequestFactory
from factories import cria_lista_nao_vazia, cria_lista_vazia, cria_item
from lista import views
from lista.forms import ItemForm, ItemNewForm
from lista.models import Item
# I usually use assert_equals instead of plain assert
# to have a comparison between expected and real on assertion error
from contrib.tests import assert_post, assert_get, assert_equals


class VerListaSpec(TestCase):  # Specification
    """
    Comportamento da view ver_lista
    """
    def setUp(self):
        self.request = RequestFactory().get('/lista/')

    def deve_saber_mostrar_lista_vazia(self):
        cria_lista_vazia()
        response = views.ver_lista(self.request)
        assert_get(response, 'lista/ver_lista.html')
        assert_equals(len(response.context_data['lista']), 0)

    def deve_saber_mostrar_lista_com_items(self):
        lista = cria_lista_nao_vazia()
        response = views.ver_lista(self.request)
        assert_get(response, 'lista/ver_lista.html')
        assert len(response.context_data['lista']) > 0
        for item in lista:
            assert item in response.context_data['lista']


class VerDetalhesItemSpec(TestCase):  # Specification
    """
    Comportamento da view ver_detalhes_item
    """
    def setUp(self):
        self.item = cria_item()

    def deve_saber_apresentar_a_pagina_corretamente(self):
        request = RequestFactory().get('/lista/%s/' % self.item.id)
        response = views.ver_detalhes_item(request, self.item.id)
        # Estamos com o Form correto no contexto passado para o template
        assert_get(response, 'lista/ver_detalhes_item.html')
        assert_equals(response.context_data['form'].__class__, ItemForm)
        # E estamos com o form carregado com a instancia de model correta
        assert_equals(response.context_data['form'].instance, self.item)

    def deve_saber_mudar_o_estado_de_completo_de_um_item(self):
        assert self.item.completo is False

        # passar de incompleto para completo
        post_data = {'completo': 1, 'nome': self.item.nome}
        response = self.client.post('/lista/%s/' % self.item.id, post_data)
        assert_post(response, '/lista/')
        # refresh da nossa instancia na memoria com as atualizacoes no DB
        self.item = Item.objects.get(id=self.item.id)
        assert self.item.completo is True

        # passar de completo para incompleto
        post_data['completo'] = 0
        response = self.client.post('/lista/%s/' % self.item.id, post_data)
        assert_post(response, '/lista/')
        # refresh da nossa instancia na memoria com as atualizacoes no DB
        self.item = Item.objects.get(id=self.item.id)
        assert self.item.completo is False


class AdicionarItemSpec(TestCase):
    """
    Comportamento da view adicionar_item
    """
    def deve_saber_apresentar_a_pagina_corretamente(self):
        request = RequestFactory().get('/lista/adicionar')
        response = views.adicionar_item(request)
        assert_get(response, 'lista/adicionar_item.html')
        assert_equals(response.context_data['form'].__class__, ItemNewForm)
