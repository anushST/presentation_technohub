"""Urls of the api app."""
from django.urls import include, path

from .views import StartAppViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', StartAppViewSet)

urlpatterns = [
    path('', include(router.urls))
]
