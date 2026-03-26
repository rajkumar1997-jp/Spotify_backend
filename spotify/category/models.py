from django.db import models

class Song(models.Model):
    CATEGORY_CHOICES = [
        ('love', 'Love Songs'),
        ('sad', 'Sad Songs'),
        ('motivation', 'Motivation Songs'),
        ('old', 'Old Songs'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category
