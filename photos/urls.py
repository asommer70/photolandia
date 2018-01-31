from django.urls import path
from . import views

app_name = 'photos'
urlpatterns = [
    path('', views.PhotoListView.as_view(), name='list'),
    path('create', views.PhotoCreateView.as_view(), name='create'),
]
