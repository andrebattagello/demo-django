# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url


@step(u'Quando eu mudar o nome do "([^"]*)" para "([^"]*)"')
def quando_eu_mudar_o_nome_do_item1_para_item2(step,
                                               item_name1, item_name2):
    world.browser.visit(django_url('/lista/'))
    world.browser.click_link_by_partial_text(item_name1)
    world.browser.find_by_value(item_name1).first.fill(item_name2)
    world.browser.find_by_value('Salvar').first.click()
