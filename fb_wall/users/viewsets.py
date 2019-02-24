from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from fb_wall.users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get']
