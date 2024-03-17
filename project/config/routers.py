from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')
urlpatterns = router.urls