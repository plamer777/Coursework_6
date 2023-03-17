"""This file contains routes for AdViewSet, UserAdsView and CommentViewSet"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from ads.views import AdViewSet, CommentViewSet, UserAdsView
# -------------------------------------------------------------------------

router = SimpleRouter()
comments_router = SimpleRouter()
router.register('ads', AdViewSet)
comments_router.register('comments', CommentViewSet)

urlpatterns = [
    path('ads/me/', UserAdsView.as_view()),
    path('', include(router.urls)),
    path('ads/<int:uid>/', include(comments_router.urls)),

]
