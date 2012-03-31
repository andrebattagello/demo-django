# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url


def mudar_status_completo_item(item_name, completo):
    world.browser.visit(django_url('/lista/'))
    world.browser.click_link_by_partial_text(item_name)
    el = world.browser.find_by_name('completo').first
    if completo:
        el.check()
    else:
        el.uncheck()
    world.browser.find_by_value('Salvar').first.click()


@step(u'Quando eu marcar o "([^"]*)" como completo')
def quando_eu_marcar_o_item_como_completo(step, item_name):
    mudar_status_completo_item(item_name, True)


@step(u'Então eu devo verificar que o "([^"]*)" realmente está completo')
def entao_eu_devo_verificar_que_o_item_realmente_esta_completo(step,
                                                               item_name):
    world.browser.visit(django_url('/lista/'))
    assert "%s ==> Completo" % item_name


@step(u'Quando eu marcar o "([^"]*)" como incompleto')
def quando_eu_marcar_o_item_como_incompleto(step, item_name):
    mudar_status_completo_item(item_name, False)


@step(u'Então eu devo verificar que o "([^"]*)" realmente está incompleto')
def entao_eu_devo_verificar_que_o_item_realmente_esta_incompleto(step,
                                                                 item_name):
    world.browser.visit(django_url('/lista/'))
    assert "%s ==> Incompleto" % item_name
