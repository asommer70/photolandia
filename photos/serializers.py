from rest_framework import serializers
from . import models


class PhotoSerializer(serializers.ModelSerializer):
    # from albums.serializers import AlbumSerializer

    filename = serializers.ReadOnlyField()
    # albums = AlbumSerializer(many=True)


    class Meta:
        fields = (
            'id',
            'image',
            'filename',
            'caption',
            'created_at',
            'updated_at',
            'albums'
        )
        model = models.Photo

    # image = serializers.FileField(read_only=True)