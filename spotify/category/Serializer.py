from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongDetailSerializer(serializers.ModelSerializer):
    media_files = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'category', 'media_files']

    def get_media_files(self, obj):
        from music.serializers import MediaFileSerializer
        media = obj.media_files.all()
        return MediaFileSerializer(media, many=True, context=self.context).data
