

from django.urls import path

from . import views


# urlpatterns = [
#     path('', views.list, name='chords_list'),
#     path('<int:pk>/', views.details, name='chords_details'),
#     path('create/', views.create, name='chords_create')
# ]

urlpatterns = [
    path('', views.ChordListView.as_view(), name='chords_list'),
    path('details/<int:pk>/', views.ChordDetailView.as_view(), name='chord_detail'),
    path('create/', views.ChordCreateView.as_view(), name='chords_create'),
    path('update/<int:pk>/', views.ChordUpdateView.as_view(), name='chords_update'),
    path('delete/<int:pk>/', views.ChordsDeleteView.as_view(), name='chords_delete')
]
