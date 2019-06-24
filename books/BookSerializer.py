from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    year = serializers.CharField()
    isbn = serializers.CharField()
    author = serializers.CharField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
