# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from lista.models import Item


def ver_lista(request):
    template_name = 'lista/ver_lista.html'
    itens = Item.objects.all()
    context = {'lista': itens}

    return TemplateResponse(request,
                            template_name,
                            context)
