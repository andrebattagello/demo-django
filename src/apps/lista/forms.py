# -*- coding: utf-8 -*-
from django import forms
from lista.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item


class ItemNewForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['completo']
