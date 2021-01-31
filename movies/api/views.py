from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie, Genre
from.serializers import MovieSerializer, GenreSerializer

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics

#Create your view here
class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CreateMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ListGenre(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class CreateGenre(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "slug"