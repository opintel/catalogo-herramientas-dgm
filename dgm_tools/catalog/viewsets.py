from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostListSerializer, PostSingleSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.select_related('category').only('id', 'text', 'title', 'slug', 'description', 'category', 'tags', 'public', 'created').all()
    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category', 'tags', 'title')

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostSingleSerializer
        return PostListSerializer
