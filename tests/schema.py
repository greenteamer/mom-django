import graphene
from graphene_django.types import DjangoObjectType

from tests.models import Test, TestQuestion, TestQuestionVariant, StudentTest, StudentTestAnswer


class TestType(DjangoObjectType):
    class Meta:
        model = Test


class TestQuestionType(DjangoObjectType):
    class Meta:
        model = TestQuestion


class TestQuestionVariantType(DjangoObjectType):
    class Meta:
        model = TestQuestionVariant


class Query(object):

    test = graphene.Field(TestType, id=graphene.Int())
    all_tests = graphene.List(TestType)

    testQuestion = graphene.Field(TestQuestionType, id=graphene.Int())
    all_test_questions = graphene.List(TestQuestionType)

    testQuestionVariant = graphene.Field(TestQuestionVariantType, id=graphene.Int())
    all_test_question_variants = graphene.List(TestQuestionVariantType)

    def resolve_test(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Test.objects.get(pk=id)
        return None

    def resolve_all_tests(self, info, **kwargs):
        return Test.objects.all()

    def resolve_test_question(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TestQuestion.objects.get(pk=id)
        return None

    def resolve_all_test_questions(self, info, **kwargs):
        return TestQuestion.objects.select_related('test').all()

    def resolve_test_question_variant(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TestQuestionVariant.objects.get(pk=id)
        return None

    def resolve_all_test_question_variants(self, info, **kwargs):
        return TestQuestionVariant.objects.select_related('question').all()

