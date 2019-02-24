from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from fb_wall.blog.models import Post
from fb_wall.blog.serializers import PostSerializer


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_posts(self, request, *args, **kwargs):
        """Get related posts of a logged-in user"""
        user = request.user
        user_posts = user.posts.all()
        page = self.paginate_queryset(user_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(user_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
