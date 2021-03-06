from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404


from . import models
from . import forms
from .serializers import PhotoSerializer


class PhotoListView(LoginRequiredMixin, ListView):
    context_object_name = 'photos'
    model = models.Photo
    paginate_by = 10


class PhotoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    fields = ['image']
    model = models.Photo
    success_url = reverse_lazy('photos:list')
    success_message = "Photo created."

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


class PhotoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ['image', 'caption', 'albums']
    model = models.Photo
    success_url = reverse_lazy('photos:list')
    success_message = "Photo updated."


class PhotoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Photo
    success_url = reverse_lazy('photos:list')
    success_message = "Photo deleted."


class ListCreatePhoto(generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication,)
    

class RetrieveUpdateDestroyPhoto(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk, format=None):
        try:
            photo = models.Photo.objects.get(pk=pk)
        except models.Photo.DoesNotExist:
            try:
                photo = models.Photo.objects.get(local_id=pk)
            except:
                raise Http404
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

