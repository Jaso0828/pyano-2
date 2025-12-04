from django.db import models


class PianoCategory(models.Model):
    model = models.CharField(max_length=150, 
                             null=False,
                             blank=False,
                             help_text='Kategorija klavira')
    
    def __str__(self):
        return f'{self.model}'
