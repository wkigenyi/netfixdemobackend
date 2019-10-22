from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from .models import Director,Actor,Movie
from .serializers import DirectorSerializer,MovieSerializer,ActorSerializer
# Create your views here.

class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieList(generics.ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer