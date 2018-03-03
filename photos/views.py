from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt


from . import models
from . import forms
from .serializers import PhotoSerializer


class PhotoListView(LoginRequiredMixin, ListView):
    context_object_name = 'photos'
    model = models.Photo
    paginate_by = 10


class PhotoCreateView(LoginRequiredMixin, CreateView):
    fields = ['image']
    model = models.Photo
    success_url = reverse_lazy('photos:list')

    def get_form(self):
        return forms.MultiPhotoForm

    def post(self, request, *args, **kwargs):
        form = forms.MultiPhotoForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                models.Photo.objects.create(image=f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['image', 'caption', 'albums']
    model = models.Photo
    success_url = reverse_lazy('photos:list')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Photo
    success_url = reverse_lazy('photos:list')


class ListCreatePhoto(generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication,)
    

class RetrieveUpdateDestroyPhoto(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication,)

