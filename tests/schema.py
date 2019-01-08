import graphene
from django import http
from graphene import relay, InputObjectType, Mutation
from graphene_django.types import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User

from tests.models import Test, TestQuestion, TestQuestionVariant


# Test
class TestType(DjangoObjectType):
    class Meta:
        model = Test


class TestQuery(object):

    test = graphene.Field(TestType, id=graphene.Int())
    all_tests = graphene.List(TestType)

    def resolve_test(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Test.objects.get(pk=id)
        return None

    def resolve_all_tests(self, info, **kwargs):
        return Test.objects.all()


# TestQuestion
class TestQuestionType(DjangoObjectType):
    class Meta:
        model = TestQuestion


class TestQuestionQuery(object):

    testQuestion = graphene.Field(TestQuestionType, id=graphene.Int())
    all_test_questions = graphene.List(TestQuestionType)

    def resolve_test_question(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TestQuestion.objects.get(pk=id)
        return None

    def resolve_all_test_questions(self, info, **kwargs):
        return TestQuestion.objects.select_related('test').all()


# TestQuestionVariant
class TestQuestionVariantType(DjangoObjectType):
    class Meta:
        model = TestQuestionVariant


class TestQuestionVariantQuery(object):

    testQuestionVariant = graphene.Field(TestQuestionVariantType, id=graphene.Int())
    all_test_question_variants = graphene.List(TestQuestionVariantType)

    def resolve_test_question_variant(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TestQuestionVariant.objects.get(pk=id)
        return None

    def resolve_all_test_question_variants(self, info, **kwargs):
        return TestQuestionVariant.objects.select_related('question').all()
