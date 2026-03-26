from rest_framework import serializers
from .models import MediaFiles
from category.models import Song

class MediaFileSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    audio = serializers.SerializerMethodField()

    class Meta:
        model = MediaFiles
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_audio(self, obj):   
        request = self.context.get('request')
        if obj.audio:
            return request.build_absolute_uri(obj.audio.url)
        return None

class SongdetailsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = MediaFiles
        fields = ['id', 'title', 'image', 'category', 'audio', 'created_at']

  