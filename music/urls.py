from django.urls import path
from .views import upload_media, get_media

urlpatterns = [
    path('upload-media/', upload_media),
    path('get-media/', get_media),
]
