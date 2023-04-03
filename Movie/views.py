from django.shortcuts import render
from . models import Movie
from rest_framework import status
from . serializers import MoviesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view([ 'GET', 'POST'])
def index(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MoviesSerializer(movie, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MoviesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view([ 'GET', 'PUT', 'DELETE'])
def detail(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response ({'error' : 'Movie does not exixt'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MoviesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk = pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        




