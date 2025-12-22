
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)

from pianos.models.pianos import Piano


def list(request):
    pianos = Piano.objects.all()
    return render(request, 'pianos/list.html', {'pianos': pianos})


class PianoListView(ListView):
    model = Piano
    


# def details(request, pk):
#     piano = get_object_or_404(
#         Piano.objects, pk=pk
#     )
#     return render(request, 'piano/detail.html', {'piano': piano})


class PianoDetailView(DetailView):
    model = Piano
    context_object_name = 'piano'


def create(request):
    # pianos = Piano.objects.all()
    return render(request, 'pianos/create.html')


class PianoCreateView(CreateView):
    model = Piano
    # fields = ['model', 'description', 'category']
    fields = '__all__'
    success_url = reverse_lazy('pianos:pianos_create')


class PianoUpdateView(UpdateView):
    model = Piano
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pianos:pianos_update')


class PianoDeleteView(DeleteView):
    model = Piano
    