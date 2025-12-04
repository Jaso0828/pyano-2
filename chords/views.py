from django.shortcuts import render, get_object_or_404

from chords.models.chords import Chord


def list(request):
    chords = Chord.objects.all()
    return render(request, 'chords/list.html', {'chords': chords})


def details(request, pk):
    chord = get_object_or_404(
        Chord.objects, pk=pk
    )
    return render(request, 'chords/details.html', {'chord': chord})

def create(request):
    # chords = Chord.objects.all()
    return render(request, 'chords/create.html')