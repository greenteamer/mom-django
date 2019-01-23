import graphene
from django import http
from graphene import relay, InputObjectType, Mutation
from graphene_django.types import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User

from tests.models import Test, TestQuestion, TestQuestionVariant
from .models import StudentTest, StudentTestAnswer
# from . import serializers


class StudentTestType(DjangoObjectType):
    class Meta:
        model = StudentTest


# StudentTest QUERY
class StudentTestQuery(object):

    studentTest = graphene.Field(StudentTestType, id=graphene.Int())
    all_student_tests = graphene.List(StudentTestType)

    def resolve_student_test(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return StudentTest.objects.get(pk=id)
        return None

    def resolve_all_student_tests(self, info, **kwargs):
        # return StudentTest.objects.select_related('test').all()
        return StudentTest.objects.all()


# StudentTest CREATE
class StudentTestCreateInput(InputObjectType):
    testId = graphene.Int(required=True)
    totalPoints = graphene.Int(required=False)


class StudentTestCreateMutation(graphene.Mutation):
    studentTest = graphene.Field(StudentTestType)

    class Arguments:
        input = StudentTestCreateInput(required=True)

    def mutate(self, info, input=None):
        try:
            test = Test.objects.get(id=input['testId'])
            studentTest = StudentTest(
                user=info.context.user,
                test=test
            )
            studentTest.full_clean()
            studentTest.save()
            return StudentTestCreateMutation(studentTest=studentTest)

        except ValidationError as e:
            return StudentTestCreateMutation(studentTest=None, errors=e)


# StudentTest UPDATE
class StudentTestUpdateInput(InputObjectType):
    id = graphene.Int(required=True)
    totalPoints = graphene.Int(required=True)


class StudentTestUpdateMutation(graphene.Mutation):
    studentTest = graphene.Field(StudentTestType)

    class Arguments:
        input = StudentTestUpdateInput(required=True)

    def mutate(self, info, input=None):
        try:
            studentTest = StudentTest.objects.get(id=input['id'])
            studentTest.totalPoints = input['totalPoints']
            studentTest.full_clean()
            studentTest.save()
            return StudentTestUpdateMutation(studentTest=studentTest)

        except ValidationError as e:
            return StudentTestUpdateMutation(studentTest=None, errors=e)


# StudentTestAnswer
# StudentTestAnswer TYPE
class StudentTestAnswerType(DjangoObjectType):
    class Meta:
        model = StudentTestAnswer


# StudentTestAnswer QUERY
class StudentTestAnswerQuery(object):

    studentTestAnswer = graphene.Field(StudentTestAnswerType, id=graphene.Int())
    all_student_test_answers = graphene.List(StudentTestAnswerType)
    all_question_answers = graphene.List(StudentTestAnswerType)
    all_variant_answers = graphene.List(StudentTestAnswerType)

    def resolve_student_test_answer(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return StudentTestAnswer.objects.get(pk=id)
        return None

    def resolve_all_student_test_answers(self, info, **kwargs):
        return StudentTestAnswer.objects.select_related('studentTestAnswers').all()

    def resolve_all_question_answers(self, info, **kwargs):
        return StudentTestAnswer.objects.select_related('questionAnswers').all()

    def resolve_all_variant_answers(self, info, **kwargs):
        return StudentTestAnswer.objects.select_related('variantAnswers').all()


# StudentTestAnswer CREATE
class StudentTestAnswerCreateInput(InputObjectType):
    testId = graphene.Int(required=True)
    variantId = graphene.Int(required=True)
    questionId = graphene.Int(required=True)
    answer = graphene.String(required=False)


class StudentTestAnswerCreateMutation(graphene.Mutation):
    studentTest = graphene.Field(StudentTestType)

    class Arguments:
        input = StudentTestAnswerCreateInput(required=True)

    def mutate(self, info, input=None):
        try:
            user = info.context.user
            studentTest = StudentTest.objects.get(id=input['testId'])
            question = TestQuestion.objects.get(id=input['questionId'])
            variant = TestQuestionVariant.objects.get(id=input['variantId'])
            answer = StudentTestAnswer(
                user=user,
                studentTest=studentTest,
                question=question,
                variant=variant,
            )
            answer.full_clean()
            answer.save()
            return StudentTestAnswerCreateMutation(studentTest=studentTest)

        except ValidationError as e:
            return StudentTestAnswerCreateMutation(studentTest=None, errors=e)
