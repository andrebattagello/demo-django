from django.test import TestCase
from lista.models import Lista


class ListaSpec(TestCase):

    def deve_comecar_vazia(self):
        lista = Lista()
        assert lista.is_empty()
