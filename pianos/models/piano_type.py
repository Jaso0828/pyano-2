from django.db import models


class PianoType(models.Model):
    model = models.CharField(max_length=150, 
                             null=False,
                             blank=False,
                             help_text='Tip klavira')

    def __str__(self):
        return f'{self.model}'
