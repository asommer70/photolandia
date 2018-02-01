from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.AlbumListView.as_view(), name='list'),
    path('create', views.AlbumCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.AlbumUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.AlbumDeleteView.as_view(), name='delete'),
]
