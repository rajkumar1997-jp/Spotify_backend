from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, get_all_songs, get_song_by_id, get_by_category

router = DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', get_all_songs),
    path('song/<int:id>/', get_song_by_id),
    path('category/<str:category>/', get_by_category),
]
