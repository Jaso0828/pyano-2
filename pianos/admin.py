from django.contrib import admin
from .models.pianos import Piano, PianoCategory, PianoType
# Register your models here.

admin.site.register([Piano, PianoType, PianoCategory])