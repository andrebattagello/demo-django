# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from lista.models import Lista, Item


@step(u'Dado que exista uma lista')
def dado_que_exista_uma_lista(step):
    world.lista = Lista()
    world.lista.save()


@step(u'E a lista está vazia')
def e_a_lista_esta_vazia(step):
    assert world.lista.is_empty()


@step(u'Quando eu ver a lista')
def quando_eu_ver_a_lista(step):
    world.response = world.browser.visit(django_url('/lista/'))


@step(u'Então eu devo ser apresentado com "([^"]*)"')
def entao_eu_devo_ser_apresentado_com_texto(step, texto):
    assert texto in world.browser.html


@step(u'E a lista contém os seguintes itens:')
def e_a_lista_contem_os_seguintes_itens(step):
    # http://lettuce.it/tutorial/tables.html#tutorial-tables
    for item_dict in step.hashes:  # step.hashes eh uma lista de dicionarios
        item = Item(**item_dict)  # search for unpacking variables (**kwargs)
        world.lista.add_item(item)
    world.lista.save()


@step(u'E eu devo ser apresentado com os seguintes itens:')
def e_eu_devo_ser_apresentado_com_os_seguintes_itens(step):
    for item in step.hashes:  # step.hashes eh uma lista de dicionarios
        assert item['nome'] in world.browser.html
