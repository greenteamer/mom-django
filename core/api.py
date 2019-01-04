from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ArticleViewSet(viewsets.ModelViewSet):
    """ViewSet for the Article class"""

    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
