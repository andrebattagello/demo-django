# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from lista.models import Item
from lista.forms import ItemForm, ItemNewForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def ver_lista(request):
    template_name = 'lista/ver_lista.html'
    itens = Item.objects.all()
    context = {'lista': itens}

    return TemplateResponse(request,
                            template_name,
                            context)


def ver_detalhes_item(request, item_id):
    template_name = 'lista/ver_detalhes_item.html'
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ver_lista'))
    else:  # GET
        form = ItemForm(instance=item)

    context = {'form': form}  # GET or Error in form validation
    return TemplateResponse(request,
                           template_name,
                           context)


def adicionar_item(request):
    template_name = 'lista/adicionar_item.html'

    if request.method == 'POST':
        form = ItemNewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ver_lista'))
    else:
        form = ItemNewForm()

    context = {'form': form}
    return TemplateResponse(request,
                           template_name,
                           context)
