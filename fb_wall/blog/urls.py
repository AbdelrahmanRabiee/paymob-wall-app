from django.urls import path

from rest_framework.routers import DefaultRouter

from fb_wall.blog.viewsets import PostsViewSet
from fb_wall.blog.views import TimeLine, AddPost

app_name = "blog"
urlpatterns = [
    path("", TimeLine.as_view(), name="timeline"),
    path("profile", AddPost.as_view(), name="profile"),

]

post_router = DefaultRouter()
post_router.register(r'posts',
                     PostsViewSet, base_name='posts')
