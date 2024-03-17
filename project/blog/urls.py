from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PostViewSet, CommentViewSet

# router

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
urlpatterns = router.urls


# urlpatterns = [
# ]