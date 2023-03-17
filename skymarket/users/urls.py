"""This file contains routes for DjoserUserViewSet and TokenObtainPairView"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import DjoserUserViewSet
# -------------------------------------------------------------------------

router = SimpleRouter()
router.register('users', DjoserUserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
    path('token/', TokenObtainPairView.as_view()),
    ]
