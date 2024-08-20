from rest_framework import routers
from django.urls import path, include
from .views import CustomUserViewSet

router = routers.DefaultRouter()
router.register('user', CustomUserViewSet, basename='user')
# router.register('contributor', ContributorViewSet, basename='contributor')
# router.register('project', ProjectViewSet, basename='project')
# router.register('issue', IssueViewSet, basename='issue')
# router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]