from rest_framework import serializers
from .models import Post


class PostSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'tags',
            'public',
            'created',
            'text'
        )


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'category',
            'tags',
            'public',
            'created',
        )
