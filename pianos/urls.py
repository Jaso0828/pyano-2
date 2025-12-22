from django.urls import path

from . import views


urlpatterns = [
    # path('', views.list, name='pianos_list'),
    # path('/<int:pk>', views.details, name='pianos_details'),
    # path('/create', views.create, name='pianos_create')
    path('', views.PianoListView.as_view(), name='pianos_list'),
    path('<int:pk>/', views.PianoDetailView.as_view(), name='piano_detail'),
    path('create/', views.PianoCreateView.as_view(), name='pianos_create'),
    path('delete/<int:pk>', views.PianoDeleteView.as_view(), name='pianos_delete'),
    path('update/<int:pk>', views.PianoUpdateView.as_view(), name='pianos_update')
]

