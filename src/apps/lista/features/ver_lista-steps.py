# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from lista.models import Lista, Item


def criar_lista_vazia():
    """
    Apenas um helper function para evitar repeticoes.
    O motivo que eu nao estou usando o factory de mesmo nome
    eh porque neste caso eu quero usar a Entidade real e nao um substituto.
    """
    lista = Lista()
    lista.save()
    return lista


@step(u'Dado que exista uma lista vazia')
def dado_que_exista_uma_lista_vazia(step):
    criar_lista_vazia()


@step(u'Quando eu ver a lista')
def quando_eu_ver_a_lista(step):
    world.response = world.browser.visit(django_url('/lista/'))


@step(u'Então eu devo ser apresentado com "([^"]*)"')
def entao_eu_devo_ser_apresentado_com_texto(step, texto):
    assert texto in world.browser.html


@step(u'Dado que exista uma lista com os seguintes itens:')
def dado_que_exista_uma_lista_com_os_seguintes_itens(step):
    lista = criar_lista_vazia()
    # http://lettuce.it/tutorial/tables.html#tutorial-tables
    for item_dict in step.hashes:  # step.hashes eh uma lista de dicionarios
        item = Item(**item_dict)  # study unpacking variables (**kwargs)
        lista.add_item(item)
    lista.save()


@step(u'E eu devo ser apresentado com os seguintes itens:')
def e_eu_devo_ser_apresentado_com_os_seguintes_itens(step):
    for item in step.hashes:  # step.hashes eh uma lista de dicionarios
        assert item['nome'] in world.browser.html
