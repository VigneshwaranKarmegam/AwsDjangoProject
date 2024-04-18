from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.creator.username}-Score:{self.score}"
    class Meta:
        ordering = ['-id']


