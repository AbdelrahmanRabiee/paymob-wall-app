from rest_framework import serializers

from fb_wall.users.models import User
from fb_wall.users.tasks import send_welcome_email


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_welcome_email.delay(user.id)
        return user


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
