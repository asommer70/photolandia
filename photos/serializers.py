from rest_framework import serializers
from . import models
from albums.models import Album
# from albums.serializers import AlbumSerializer


class PhotoSerializer(serializers.ModelSerializer):
    # albums = AlbumSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'image',
            'filename',
            'caption',
            'local_filename',
            'local_id',
            'local_path',
            'created_at',
            'updated_at',
            'albums',
        )
        model = models.Photo