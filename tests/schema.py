import graphene
from django import http
from graphene import relay, InputObjectType, Mutation
from graphene_django.types import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User

from tests.models import Test, TestQuestion, TestQuestionVariant, StudentTest, StudentTestAnswer
from . import serializers


class TestType(DjangoObjectType):
    class Meta:
        model = Test


class TestQuestionType(DjangoObjectType):
    class Meta:
        model = TestQuestion


class TestQuestionVariantType(DjangoObjectType):
    class Meta:
        model = TestQuestionVariant


class StudentTestType(DjangoObjectType):
    class Meta:
        model = StudentTest


class StudentTestAnswerType(DjangoObjectType):
    class Meta:
        model = StudentTestAnswer


class Query(object):

    # tests
    test = graphene.Field(TestType, id=graphene.Int())
    all_tests = graphene.List(TestType)

    # questions
    testQuestion = graphene.Field(TestQuestionType, id=graphene.Int())
    all_test_questions = graphene.List(TestQuestionType)

    # variants
    testQuestionVariant = graphene.Field(TestQuestionVariantType, id=graphene.Int())
    all_test_question_variants = graphene.List(TestQuestionVariantType)

    # student tests
    studentTest = graphene.Field(StudentTestType, id=graphene.Int())
    all_student_tests = graphene.List(StudentTestType)

    # student test answers
    studentTestAnswer = graphene.Field(StudentTestAnswerType, id=graphene.Int())
    all_student_test_answers = graphene.List(StudentTestAnswerType)
    all_question_answers = graphene.List(StudentTestAnswerType)
    all_variant_answers = graphene.List(StudentTestAnswerType)

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

    def resolve_student_test(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return StudentTest.objects.get(pk=id)
        return None

    def resolve_all_student_tests(self, info, **kwargs):
        # return StudentTest.objects.select_related('test').all()
        return StudentTest.objects.all()

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


class StudentTestAnswerMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.StudentTestAnswerSerializer
    
    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        user = info.context.user
        requestedUser = User.objects.get(id=input['user'])
        # input['user'] = '' + user.id
        # print('>>> input %s', input)
        if user.id != requestedUser.id:
            raise Exception('Authorization failed')

        if 'id' in input:
            test = StudentTest.objects.get(id=input['studentTest'], user=user)
            instance = StudentTestAnswer.objects.get(id=input['id'], studentTest=test)
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}
            else:
                raise Exception('No such StudentTestAnswer')

        return {'data': input, 'partial': True}


# class StudentTestMutation(SerializerMutation):
#     class Meta:
#         serializer_class = serializers.StudentTestSerializer
    
#     @classmethod
#     def get_serializer_kwargs(cls, root, info, **input):
#         if 'id' in input:
#             user = info.context.user
#             instance = StudentTest.objects.get(id=input['id'], user=user)
#             if instance:
#                 return {'instance': instance, 'data': input, 'partial': True}
#             else:
#                 raise Exception('No such StudentTest')

#         return {'data': input, 'partial': True}


class StudentTestCreateInput(InputObjectType):
    test = graphene.Int()
    totalPoints = graphene.Int(required=False)


class CreateStudentTestMutation(graphene.Mutation):
    studentTest = graphene.Field(StudentTestType)

    class Arguments:
        input = StudentTestCreateInput(required=True)

    @login_required
    def mutate(self, info, input=None):
        try:
            test = StudentTest()
            return test

        except ValidationError as e:
            return None

