from django.urls import path

from rest_framework.routers import DefaultRouter

from fb_wall.users.views import SignUp, SignIn
from fb_wall.users.viewsets import UserViewSet

app_name = "users"
urlpatterns = [
    path("", SignUp.as_view(), name="signup"),
    path("signin/", SignIn.as_view(), name="signin"),

]


user_router = DefaultRouter()
user_router.register(r'user', UserViewSet, base_name='user')
