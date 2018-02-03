from rest_framework import serializers
from . import models
# from albums.serializers import AlbumSerializer


class PhotoSerializer(serializers.ModelSerializer):
	# albums = AlbumSerializer(read_only=True, many=True)
    class Meta:
        fields = (
            'id',
            'image',
            'caption',
            'created_at',
            'updated_at',
        )
        model = models.Photo

    image = serializers.FileField(read_only=True)