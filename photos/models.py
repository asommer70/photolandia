from django.db import models
from albums.models import Album

class Photo(models.Model):
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.image.name
