from . import models

from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Test
        fields = (
            'id',
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
            'id',
            'pk', 
            'name', 
            'text', 
            'points', 
            'test',
        )


class TestQuestionVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestQuestionVariant
        fields = (
            'id',
            'pk', 
            'name', 
            'value', 
            'question', 
        )


class StudentTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentTest
        fields = (
            'id',
            'pk', 
            'totalPoints', 
        )


class StudentTestAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StudentTestAnswer
        fields = (
            'id',
            'pk', 
        )


