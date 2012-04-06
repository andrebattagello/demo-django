# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from lista.models import Item


def cria_lista_vazia():
    return []


@step(u'Dado que exista uma lista vazia')
def dado_que_exista_uma_lista_vazia(step):
    cria_lista_vazia()


@step(u'Quando eu ver a lista')
def quando_eu_ver_a_lista(step):
    world.response = world.browser.visit(django_url('/lista/'))


@step(u'Então eu devo ser apresentado com "([^"]*)"')
def entao_eu_devo_ser_apresentado_com_texto(step, texto):
    assert world.browser.is_text_present(texto)
    #assert texto in world.browser.html


@step(u'Dado que exista uma lista com os seguintes itens:')
def dado_que_exista_uma_lista_com_os_seguintes_itens(step):
    lista = cria_lista_vazia()
    # http://lettuce.it/tutorial/tables.html#tutorial-tables
    for item_dict in step.hashes:  # step.hashes eh uma lista de dicionarios
        item = Item(**item_dict)  # study unpacking variables (**kwargs)
        item.save()
        lista.append(item)
    world.lista = lista


@step(u'E eu devo ser apresentado com os seguintes itens:')
def e_eu_devo_ser_apresentado_com_os_seguintes_itens(step):
    from utils import is_step_items_present
    assert is_step_items_present(step)
