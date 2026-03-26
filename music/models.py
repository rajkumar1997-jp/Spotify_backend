from django.db import models
from category.models import Song

class MediaFiles(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    
    category = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='media_files'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
