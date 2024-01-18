from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'api/v1/posts', PostViewSet)
v1_router.register(r'api/v1/groups', GroupViewSet)
v1_router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('', include(v1_router.urls)),
]
