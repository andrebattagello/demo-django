# -*- coding: utf-8 -*-
import factory
from lista.models import Lista, Item


class ListaFactory(factory.Factory):
    FACTORY_FOR = Lista


class ItemFactory(factory.Factory):
    FACTORY_FOR = Item

    nome = factory.Sequence(lambda n: 'Item %s' % n)
    completo = False
    lista_pai = factory.SubFactory(ListaFactory)


def cria_lista_vazia():
    """
    Cria uma lista sem nenhum elemento
    """
    return ListaFactory()


def cria_item(lista=None):
    """
    Cria um item usando ItemFactory.
    Se o argumento opcional lista for passado, usa ele na construcao.
    """
    if not lista:
        return ItemFactory()  # usa SubFactory, pois nao pode ter None como FK
    return ItemFactory(lista_pai=lista)


def cria_lista_nao_vazia():
    """
    Cria uma lista com alguns items
    """
    lista = ListaFactory()
    for x in range(1, 10):
        cria_item(lista=lista)  # Passa para o arg opcional lista, a var lista
    return lista
