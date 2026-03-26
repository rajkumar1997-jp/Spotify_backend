from rest_framework import viewsets
from .models import Song
from .Serializer import SongSerializer, SongDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


@api_view(['GET'])
def get_all_songs(request):
    data = Song.objects.all()
    serializer = SongDetailSerializer(data, many=True, context={'request': request})

    return Response({
        "status": True,
        "data": serializer.data
    })


@api_view(['GET'])
def get_song_by_id(request, id):
    data = Song.objects.get(id=id)
    serializer = SongDetailSerializer(data, context={'request': request})

    return Response({
        "status": True,
        "data": serializer.data
    })


@api_view(['GET'])
def get_by_category(request, category):
    data = Song.objects.filter(category=category)
    serializer = SongDetailSerializer(data, many=True, context={'request': request})

    return Response({
        "status": True,
        "data": serializer.data
    })
