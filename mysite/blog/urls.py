from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, post_detail, create_comment, home

app_name = "blog"


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/create_comment/', create_comment, name='create_comment'),
]