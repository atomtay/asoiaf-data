from rest_framework import serializers
from .models import Book, Character


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.HyperlinkedRelatedField(
    #     view_name='book-detail',
    #     read_only=True
    # )

    class Meta:
        model = Book
        fields = ('id', 'title', 'num_of_chapters')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.HyperlinkedRelatedField(
    #     view_name='character-detail',
    #     read_only=True
    # )
    # book_of_death = serializers.HyperlinkedRelatedField(
    #     view_name='book-detail',
    #     read_only=True
    # )

    class Meta:
        model = Character
        fields = ('id', 'name', 'book_of_death', 'chapter_of_death',
                  'manner_of_death', 'gender', 'is_nobility')
