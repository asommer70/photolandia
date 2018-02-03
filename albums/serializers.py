from rest_framework import serializers
from . import models
from photos.serializers import PhotoSerializer


class AlbumSerializer(serializers.ModelSerializer):
    photo_set = PhotoSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'photo_set'
        )
        model = models.Album

