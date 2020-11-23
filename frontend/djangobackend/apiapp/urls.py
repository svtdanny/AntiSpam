from django.urls import path
from . views import PostsView, LearnSetsView

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('posts/', PostsView.as_view()),
    path('profile/get/', PostsView.as_view()),
]