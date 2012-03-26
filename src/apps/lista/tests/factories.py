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
from lista.models import Item


class ItemFactory(factory.Factory):
    FACTORY_FOR = Item

    nome = factory.Sequence(lambda n: 'Item %s' % n)
    completo = False


def cria_lista_vazia():
    """
    Cria uma lista vazia
    """
    return []


def cria_item():
    """
    Cria um item usando ItemFactory.
    """
    return ItemFactory()  # usa o lista que foi passado


def cria_lista_nao_vazia():
    """
    Cria uma lista com alguns items.
    """
    lista = []
    for x in range(0, 10):  # serao 10 itens nesta lista
        item = cria_item()  # Passa para o arg opcional lista, a var lista
        lista.append(item)
    return lista
