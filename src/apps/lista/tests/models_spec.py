# -*- coding: utf-8 -*-
"""
Contém Specifications de teste
que descrevem o comportamento dos models deste app

"""
from django.test import TestCase
# I usually use assert_equals instead of plain assert
# to have a comparison between expected and real on assertion error
from nose.tools import assert_equals
from lista.models import Item


class ItemSpec(TestCase):  # Specification
    """
    Comportamento do model Item
    """
    def deve_ter_um_nome(self):
        item = Item(nome='Item 1')
        item.save()
        assert_equals(item.nome, 'Item 1')

    def deve_comecar_nao_completo(self):
        item = Item(nome='Item 1')
        assert item.completo is False
