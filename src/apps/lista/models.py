from django.db import models


class Lista(models.Model):
    """
    Uma Lista de itens
    ``lista.itens`` vai conter a relacao completa de itens em ``lista``
    """

    def is_empty(self):
        return not bool(self.itens.count())

    def add_item(self, item):
        self.itens.add(item)


class Item(models.Model):
    """
    Um item de alguma lista.
    ``lista.itens`` vai conter a relacao completa de itens em ``lista``
    """
    nome = models.CharField(max_length=512, blank=False)
    completo = models.BooleanField(default=False)
    lista_pai = models.ForeignKey(Lista, related_name='itens')
