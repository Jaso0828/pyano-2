from django.db import models

class ChordType(models.Model):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        help_text='Tip akorda'
    )

    def __str__(self):
        return f'{self.name}'