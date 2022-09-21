from django.http import Http404
from .models import Music
from .serializers import MusicSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from music import serializers

# Create your views here.
class MusicList(APIView):

    def get(self, request):
        all_music = Music.objects.all()
        serializer = MusicSerializer(all_music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicDetail(APIView):

    def get_object(self,pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        music = self.get_object(pk)
        custom_response = {
            "Song Deleted": music.title
        }
        music.delete()
        return Response(custom_response, status=status.HTTP_200_OK)