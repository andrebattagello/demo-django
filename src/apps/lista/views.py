# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse


def ver_lista(request):
    template_name = 'lista/ver_lista.html'
    context = {}

    return TemplateResponse(request,
                            template_name,
                            context)
