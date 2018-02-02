from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

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
