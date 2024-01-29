from rest_framework import serializers
from .models import Anime, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True, source="genre")
    class Meta:
        model = Anime
        fields = ['id', 'title', 'studio', 'episodes', 'genres']