from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tgdjango.app.views import MessageResponseViewSet, ProfileViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('messages', MessageResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
