from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
import json

from . import models
from .serializers import AlbumSerializer

from photos.models import Photo

class AlbumListView(LoginRequiredMixin, ListView):
    context_object_name = 'albums'
    model = models.Album


class AlbumCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    fields = ['name', 'description']
    model = models.Album
    success_url = reverse_lazy('albums:list')
    success_message = "Albu  was created."


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = models.Album


class AlbumUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ['name', 'description']
    model = models.Album
    success_message = "Album was updated."


class AlbumDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Album
    success_url = reverse_lazy('albums:list') 
    success_message = "Album was deleted."


def unsorted(request):
    photo_list = Photo.objects.filter(albums=None)
    paginator = Paginator(photo_list, 10) 

    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request, 'albums/unsorted.html', {'photos': photos})


class ListCreateAlbum(generics.ListCreateAPIView):
    queryset = models.Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication,)


class RetrieveUpdateDestroyAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication,)


# @login_required
@csrf_exempt
def add_photos(request, pk):
    if request.method == 'POST':
        req_token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        token = Token.objects.get(key=req_token)

        if not token:
            return HttpResponseRedirect(reverse('photos:list'))
        else:
            album = models.Album.objects.get(id=pk)
            for photo_id in request.POST['photo_ids'].split(','):
                print('photo_id:', photo_id)
                photo = Photo.objects.get(id=photo_id)
                album.photo_set.add(photo)
                album.save()
            return JsonResponse({'message': "Photos have been added to {}.".format(album.name)})
    else: 
        return HttpResponseRedirect(reverse('photos:list'))


@csrf_exempt
def remove_photos(request, pk):
    if request.method == 'POST':
        req_token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        token = Token.objects.get(key=req_token)

        if not token:
            return HttpResponseRedirect(reverse('photos:list'))
        else:
            album = models.Album.objects.get(id=pk)
            for photo_id in request.POST['photo_ids'].split(','):
                print('photo_id:', photo_id)
                photo = Photo.objects.get(id=photo_id)
                album.photo_set.remove(photo)
                album.save()
            return JsonResponse(json.dumps(album))
    else: 
        return HttpResponseRedirect(reverse('album:detail', args=[pk]))