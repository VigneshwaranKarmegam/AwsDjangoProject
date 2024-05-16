from rest_framework import serializers
from .models import Movie, MovieDetailLink
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')
    MovieDetailLinks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator','MovieDetailLinks')

class MovieDetailLinkSerializer(serializers.ModelSerializer):  # create class to serializer model
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = MovieDetailLink
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
