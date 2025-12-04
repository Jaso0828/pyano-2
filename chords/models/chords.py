from django.db import models

from .chords_type import ChordType

class Chord(models.Model):
    name = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        help_text='Naziv akorda'
    )

    symbol = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        help_text='Simbol akorda'
    )

    scheme_url = models.CharField(
        max_length=750,
        null=True,
        blank=True,
        help_text='Putanja do sheme akorda'
    )

    type = models.ForeignKey(
        ChordType,
        null=False,
        default=0,
        on_delete=models.SET_DEFAULT
    )

    def __str__(self):
        return f'{self.name}'