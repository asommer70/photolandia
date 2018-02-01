from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

class PhotoListView(LoginRequiredMixin, ListView):
    context_object_name = 'photos'
    model = models.Photo

#
# class PhotoCreateView(LoginRequiredMixin, CreateView):
#     fields = ['image']
#     model = models.Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    fields = ['image', 'caption']
    model = models.Photo
    success_url = reverse_lazy('photos:list')


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['image', 'caption']
    model = models.Photo
    success_url = reverse_lazy('photos:list')
