from rest_framework import serializers
from . import models
# from albums.serializers import AlbumSerializer


class PhotoSerializer(serializers.ModelSerializer):
	# albums = AlbumSerializer(read_only=True, many=True)
    filename = serializers.ReadOnlyField()

    class Meta:
        fields = (
            'id',
            'image',
            'filename',
            'caption',
            'created_at',
            'updated_at',
        )
        model = models.Photo

    image = serializers.FileField(read_only=True)