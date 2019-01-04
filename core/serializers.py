from . import models

from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'text', 
        )
