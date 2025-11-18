from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer


class MovieViewSet(ViewSet):
    def list(self, request):
        movies = Movie.objects.all()
        ser = MovieSerializer(movies, many=True)
        return Response(ser.data)

    def retrieve(self, request, pk=None):
        movie = Movie.objects.get(pk=pk)
        ser = MovieSerializer(movie)
        return Response(ser.data)

    def create(self, request):
        ser = MovieSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def update(self, request, pk=None):
        movie = Movie.objects.get(pk=pk)
        ser = MovieSerializer(movie, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def destroy(self, request, pk=None):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({"message": "Deleted"})


class CommentViewSet(ViewSet):
    def list(self, request):
        com = Comment.objects.all()
        ser = CommentSerializer(com, many=True)
        return Response(ser.data)

    def retrieve(self, request, pk=None):
        com = Comment.objects.get(pk=pk)
        ser = CommentSerializer(com)
        return Response(ser.data)

    def create(self, request):
        ser = CommentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def update(self, request, pk=None):
        com = Comment.objects.get(pk=pk)
        ser = CommentSerializer(com, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def destroy(self, request, pk=None):
        com = Comment.objects.get(pk=pk)
        com.delete()
        return Response({"message": "Deleted"})
