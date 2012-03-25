from django.db import models


class Lista(models.Model):
    """
    Uma Lista de itens
    """

    def is_empty(self):
        return True
