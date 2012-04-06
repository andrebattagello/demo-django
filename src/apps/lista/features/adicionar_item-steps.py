# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url


@step(u'Quando eu adicionar o item "([^"]*)" a lista')
def quando_eu_adicionar_o_item_name_a_lista(step, name):
    world.browser.visit(django_url('/lista/'))
    world.browser.click_link_by_partial_text('Adicionar item')
    world.browser.fill('nome', name)
    world.browser.find_by_value('Salvar').first.click()


@step(u'Então eu devo ser apresentado com os seguintes itens:')
def entao_eu_devo_ser_apresentado_com_os_seguintes_itens(step):
    from utils import is_step_items_present
    assert is_step_items_present(step)
