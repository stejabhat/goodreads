from rest_framework import serializers
from .models import Book, ReadingList

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = '__all__'
        read_only_fields = ['user']  # Ensure user is auto-assigned
