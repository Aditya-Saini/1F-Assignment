from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Collection
from rest_framework.response import Response
from rest_framework import status
import uuid

COMMON_FIELDS = [
    'created_on',
    'last_updated'
]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'genres',
            'uuid'
        ]

class CollectionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    class Meta:
        model = Collection
        fields = [
            'title',
            'description',
            'movie',
        ]
    def create(self, validated_data):
        validated_data["uuid"] = uuid.uuid4()
        validated_data["user"] = self.context["request"].user
        movie = validated_data.pop("movie")
        collection = Collection.objects.create(**validated_data)
        for movie_data in movie:
            m, created = Movie.objects.get_or_create(title = movie_data.get("title",""), description = movie_data.get("description",""), uuid = movie_data.get("uuid",""), genres = movie_data.get("genres",""))
            collection.movie.add(m)
        # collection.save()
        return collection
    def update(self, instance,validated_data):
        validated_data["user"] = self.context["request"].user
        movie = validated_data.pop("movie")
        instance = super().update(instance, validated_data)
        for movie_data in movie:
            m, created = Movie.objects.get_or_create(title = movie_data.get("title",""), description = movie_data.get("description",""), uuid = movie_data.get("uuid",""), genres = movie_data.get("genres",""))
            instance.movie.add(m)
        instance.save()
        return instance