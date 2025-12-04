from django.urls import path

from . import views


urlpatterns = [
    path('', views.list, name='pianos_list'),
    path('/<int:pk>', views.details, name='pianos_details'),
    path('/create', views.create, name='pianos_create')
]

