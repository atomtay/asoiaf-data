from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('books', views.AllBooks.as_view(), name="all-books"),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book-detail'),
    path('characters', views.AllCharacters.as_view(), name='all-characters'),
    path('characters/<int:pk>', views.CharacterDetail.as_view(),
         name='character-detail')
]
