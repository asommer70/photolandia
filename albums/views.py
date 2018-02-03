from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from photos.models import Photo

class AlbumListView(LoginRequiredMixin, ListView):
    context_object_name = 'albums'
    model = models.Album


class AlbumCreateView(LoginRequiredMixin, CreateView):
    fields = ['name', 'description']
    model = models.Album
    success_url = reverse_lazy('albums:list')


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = models.Album


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', 'description']
    model = models.Album


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Album
    success_url = reverse_lazy('albums:list')



def unsorted(request):
    photo_list = Photo.objects.filter(albums=None)
    paginator = Paginator(photo_list, 10) 

    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request, 'albums/unsorted.html', {'photos': photos})