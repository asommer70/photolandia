from django.db import models
from albums.models import Album

class Photo(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='%Y/%m/')
    caption = models.TextField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    albums = models.ManyToManyField(Album, blank=True, null=True)

    def filename(self):
    	return self.image.name.split('/')[-1]

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.image.name
