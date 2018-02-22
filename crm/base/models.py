from django.db import models


class Azienda(models.Model):
    """
    Modello dati per gestire un'azienda
    """

    CATEGORIA_CHOICES = [
        ["info", "Informatica"],
        ["comm", "Commerciale"],
        ["edil", "Ediliza"],
    ]

    nome = models.CharField(max_length=30)
    codice = models.CharField(max_length=30, unique=True)
    indirizzo = models.CharField(max_length=200, null=True, blank=True)
    citta = models.CharField('Città', max_length=200, null=True, blank=True)
    categoria_cliente = models.CharField(max_length=20, null=True, blank=True, choices=CATEGORIA_CHOICES)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.nome, self.codice)

    class Meta:
        verbose_name_plural = "Aziende"
        ordering = ["nome", "codice"]
