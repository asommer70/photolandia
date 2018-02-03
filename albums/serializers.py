from rest_framework import serializers
from . import models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
        )
        model = models.Album