from . import models

from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Test
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'text', 
        )


class TestQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestQuestion
        fields = (
            'pk', 
            'name', 
            'text', 
            'points', 
        )


class TestQuestionVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestQuestionVariant
        fields = (
            'pk', 
            'name', 
            'value', 
        )


class StudentTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentTest
        fields = (
            'pk', 
            'totalPoints', 
        )


class StudentTestAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentTestAnswer
        fields = (
            'pk', 
        )


