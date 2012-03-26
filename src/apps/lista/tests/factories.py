# -*- coding: utf-8 -*-
"""
Este arquivo nao é de teste propriamente dito.
Ele é um helper para os meus testes.

Estou usando factory_boy para me ajudar a criar as dependecias para os tests.

As instancias criadas por factory_boy são persistidas
(a menos que voce impeça ele de fazer isso).

Como não estamos preocupados em mockar o DB (nao vale o esforço)
e o Django sobre um DB de testes na memoria RAM, isso normalmente está oK.

Confira mais sobre factory_boy em:
    http://readthedocs.org/docs/factoryboy/en/latest/
    http://readthedocs.org/docs/factoryboy/en/latest/subfactory.html

"""
import factory  # importa factory_boy para me ajudar
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
    Se algum argumento (opcional) ``lista`` for passado, use ele na construcao
    """
    if not lista:  # nao passou nada (chegou None nesta linha)
        return ItemFactory()  # usa SubFactory, pois nao pode ter None como FK
    return ItemFactory(lista_pai=lista)  # usa o lista que foi passado


def cria_lista_nao_vazia():
    """
    Cria uma lista com alguns items.
    """
    lista = ListaFactory()
    for x in range(1, 10):  # serao 10 itens nesta lista
        cria_item(lista=lista)  # Passa para o arg opcional lista, a var lista
    return lista
