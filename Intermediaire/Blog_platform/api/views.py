from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
