from django.db import models
from pianos.models.piano_category import PianoCategory
from pianos.models.piano_type import PianoType

# Create your models here.
class Piano(models.Model):
    model = models.CharField(max_length=150, 
                             null=False,
                             blank=False,
                             help_text='Naziv klavira')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis klavira')

    category = models.ForeignKey(PianoCategory, 
                                 default=0,
                                 on_delete=models.SET_DEFAULT)


    type = models.ForeignKey(PianoType, 
                                 default=0,
                                 on_delete=models.SET_DEFAULT)
    
    picture_url = models.CharField(max_length=750,
                                   null=True,
                                   blank=True
                                    )
    
    def __str__(self):
        return f'{self.model} {self.category} {self.type} {self.description}'

