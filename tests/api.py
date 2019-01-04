from . import models
from . import serializers
from rest_framework import viewsets, permissions


class TestViewSet(viewsets.ModelViewSet):
    """ViewSet for the Test class"""

    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestQuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the TestQuestion class"""

    queryset = models.TestQuestion.objects.all()
    serializer_class = serializers.TestQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestQuestionVariantViewSet(viewsets.ModelViewSet):
    """ViewSet for the TestQuestionVariant class"""

    queryset = models.TestQuestionVariant.objects.all()
    serializer_class = serializers.TestQuestionVariantSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentTestViewSet(viewsets.ModelViewSet):
    """ViewSet for the StudentTest class"""

    queryset = models.StudentTest.objects.all()
    serializer_class = serializers.StudentTestSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentTestAnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for the StudentTestAnswer class"""

    queryset = models.StudentTestAnswer.objects.all()
    serializer_class = serializers.StudentTestAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


