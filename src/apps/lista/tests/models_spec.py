# -*- coding: utf-8 -*-
"""
Contém Specifications de teste
que descrevem o comportamento dos models deste app

"""
from django.test import TestCase
# I usually use assert_equals instead of plain assert
# to have a comparison between expected and real on assertion error
from contrib.tests import  assert_equals
from lista.models import Item


class ItemSpec(TestCase):  # Specification
    """
    Comportamento do model Item
    """
    def setUp(self):
        self.item = Item(nome='Item 1')
        self.item.save()

    def deve_ter_um_nome(self):
        assert_equals(self.item.nome, 'Item 1')

    def deve_comecar_nao_completo(self):
        assert self.item.completo is False

    def deve_saber_a_sua_url_absoluta(self):
        assert_equals(self.item.get_absolute_url(),
                      '/lista/%s/' % self.item.id)

    def deve_saber_traduzir_para_texto_se_esta_completo(self):
        self.item.completo = 0
        assert_equals(self.item.completo_texto, 'Incompleto')
        self.item.completo = 1
        assert_equals(self.item.completo_texto, 'Completo')
