from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AnimeSerializer, GenreSerializer
from .models import Anime, Genre
from rest_framework import status

# Create your views here.
@api_view(["GET", "POST"])
def get_data(request):
    if request.method == "GET":
        item = Anime.objects.all()
        serializer = AnimeSerializer(item, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(["GET", "PUT", "DELETE"])
def addData(request, id):
    try:
        anime = Anime.objects.get(pk=id)
    except Anime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = AnimeSerializer(anime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)