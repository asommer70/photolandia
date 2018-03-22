from django.db import models
from django.urls import reverse_lazy


class Album(models.Model):
	name = models.CharField(max_length=255, null=True, unique=True)
	description = models.TextField(max_length=2048, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
	    return self.name

	def get_absolute_url(self):
	    return reverse_lazy('albums:detail', args=[self.id])

	class Meta:
		ordering = ['-updated_at']