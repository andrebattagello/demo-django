# -*- coding: utf-8 -*-
from django.test import TestCase
# I usually use assert_equals instead of plain assert
# to have a comparison between expected and real on assertion error
from nose.tools import assert_equals
from lista.models import Lista, Item
from factories import cria_item, cria_lista_nao_vazia, cria_lista_vazia


class ListaSpec(TestCase):
    """
    Comportamento do model Lista
    """
    def setUp(self):
        self.lista = Lista()  # apenas cria na memoria
        self.lista.save()  # persiste no DB

    def deve_comecar_vazia(self):
        assert self.lista.is_empty() is True

    def deve_poder_adicionar_item(self):
        item = cria_item()  # O item eh somente uma dependencia burra
                            # O SUT (System Under Test) aqui eh a lista
        self.lista.add_item(item)
        assert self.lista.is_empty() is False
        assert item in self.lista.itens.all()


class ItemSpec(TestCase):
    """
    Comportamento do model Item
    """
    def deve_ter_um_nome(self):
        lista = cria_lista_vazia()
        item = Item(nome='Item 1', lista_pai=lista)
        item.save()
        assert_equals(item.nome, 'Item 1')

    def deve_comecar_nao_completo(self):
        item = Item(nome='Item 1')
        assert item.completo is False

    def deve_conseguir_acessar_lista_pai(self):
        lista = cria_lista_nao_vazia()  # agora eh a lista que eh a dependecia
        algum_item = lista.itens.all()[0]
        assert_equals(algum_item.lista_pai, lista)
