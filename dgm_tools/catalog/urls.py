from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .viewsets import PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
