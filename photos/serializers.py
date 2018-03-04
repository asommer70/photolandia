from rest_framework import serializers
from . import models
from albums.models import Album
# from albums.serializers import AlbumSerializer


class PhotoSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'image',
            'filename',
            'caption',
            'created_at',
            'updated_at',
            'albums',
        )
        model = models.Photo