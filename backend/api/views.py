"""Views of the api app."""
from rest_framework import serializers
from rest_framework import viewsets

from .models import StartApp


class StartAppSerializer(serializers.ModelSerializer):
    """Start app serializer."""

    class Meta:
        model = StartApp
        fields = '__all__'


class StartAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StartApp.objects.all()
    serializer_class = StartAppSerializer
