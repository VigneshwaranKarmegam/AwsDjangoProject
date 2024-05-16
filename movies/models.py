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

class MovieDetailLink(models.Model):
    movie = models.ForeignKey(Movie, related_name='MovieDetailLinks', on_delete=models.CASCADE)
  #  movie_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    audio_types = models.CharField(max_length=100)
    rating = models.IntegerField()
    no_of_reviewers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='c_moviedetaillinks', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', related_name='u_moviedetaillinks', on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.updated_by.username}"
    class Meta:
        ordering = ['movie', 'updated_at']

