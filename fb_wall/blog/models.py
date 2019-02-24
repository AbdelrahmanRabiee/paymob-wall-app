from django.db import models

from django_extensions.db.models import TimeStampedModel

from fb_wall.users.models import User


# Create your models here.
class Post(TimeStampedModel):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(max_length=140)

    class Meta:
        verbose_name = 'posts'
        verbose_name_plural = 'posts'
