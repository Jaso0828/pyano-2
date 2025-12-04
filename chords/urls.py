

from django.urls import path

from . import views


urlpatterns = [
    path('', views.list, name='chords_list'),
    path('/<int:pk>', views.details, name='chords_details'),
    path('/create', views.create, name='chords_create')
]