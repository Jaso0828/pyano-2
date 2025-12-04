from django.contrib import admin
from .models.chords import Chord, ChordType

# Register your models here.
admin.site.register(Chord)
admin.site.register(ChordType)