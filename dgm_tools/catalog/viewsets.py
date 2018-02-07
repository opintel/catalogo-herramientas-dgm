from django_filters import rest_framework as filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostListSerializer, PostSingleSerializer


class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
            'tags': ['exact', 'contains'],
            'title': ['exact', 'contains', 'startswith', 'icontains']
        }


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.select_related('category').only(
        'id',
        'text',
        'title',
        'slug',
        'description',
        'category',
        'tags',
        'public',
        'created'
    ).prefetch_related('tags', 'category').filter(public=True)

    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostSingleSerializer

        return PostListSerializer
