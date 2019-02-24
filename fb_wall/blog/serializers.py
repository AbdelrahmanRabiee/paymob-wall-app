from rest_framework import serializers

from fb_wall.blog.models import Post
from fb_wall.users.serializers import UserPostSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserPostSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created']
