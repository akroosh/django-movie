from rest_framework import serializers
from .models import Movie, Genre
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class GenreGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'title'

    @receiver(pre_save)
    def my_callback(sender, instance, *args, **kwargs):
        instance.slug = slugify(instance.title)

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreGetSerializer
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Movie
        exclude = ['id']

    @receiver(pre_save)
    def my_callback(sender, instance, *args, **kwargs):
        instance.slug = slugify(instance.title)

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer
    movies = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    class Meta:
        model = Genre
        exclude = ['id']

    @receiver(pre_save)
    def my_callback(sender, instance, *args, **kwargs):
        instance.slug = slugify(instance.title)