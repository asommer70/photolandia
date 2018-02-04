from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.AlbumListView.as_view(), name='list'),
    path('create', views.AlbumCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.AlbumUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.AlbumDeleteView.as_view(), name='delete'),
    path('unsorted', views.unsorted, name='unsorted'),

    path('api', views.ListCreateAlbum.as_view(), name="albums"),
    path('api/<int:pk>', views.RetrieveUpdateDestroyAlbum.as_view(), name="album"),
    path('api/<int:pk>/add_photos', views.add_photos, name="api_add_photos"),
    path('api/<int:pk>/remove_photos', views.remove_photos, name="api_remove_photos"),
]
