from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import MediaFiles
from .serializers import MediaFileSerializer, SongdetailsSerializer

@api_view(['POST'])
def upload_media(request):
    serializer = MediaFileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Image and Audio uploaded successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_media(request):
    data = MediaFiles.objects.all()
    serializer = SongdetailsSerializer(data, many=True, context={'request': request})
    return Response({
        "status": True,
        "data": serializer.data
    })

