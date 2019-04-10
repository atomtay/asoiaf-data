from rest_framework import generics
from .serializers import BookSerializer, CharacterSerializer
from .models import Book, Character
from django.shortcuts import render
import requests

api_url_base = 'http://localhost:8000'


def homepage(request):
    response = requests.get(api_url_base+"/characters").json()
    return render(request, 'asoiaf/homepage.html', {'characters': response})


class AllBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AllCharacters(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
