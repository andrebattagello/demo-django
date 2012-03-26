from django.db import models


class Item(models.Model):
    """
    Um item de alguma lista.
    ``lista.itens`` vai conter a relacao completa de itens em ``lista``
    """
    nome = models.CharField(max_length=512, blank=False)
    completo = models.BooleanField(default=False)
