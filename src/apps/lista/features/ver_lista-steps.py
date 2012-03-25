# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from lista.models import Lista


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
