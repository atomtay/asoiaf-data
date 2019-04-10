# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Character, Nobility, Death, Book_of_Death, Chapter_of_Death
# Register your models here.


admin.site.register([Book, Character, Nobility, Death,
                     Book_of_Death, Chapter_of_Death])
