from .models import Book, Character, Nobility, Death, Book_of_Death, Chapter_of_Death
from django.shortcuts import render
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


def homepage(request):
    female_chars = len(Character.objects.filter(gender="Female"))
    male_chars = len(Character.objects.filter(gender="Male"))
    return render(request, 'asoiaf/homepage.html', {'female_chars': female_chars, 'male_chars': male_chars})
