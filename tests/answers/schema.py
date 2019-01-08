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


# StudentTest
class StudentTestType(DjangoObjectType):
    class Meta:
        model = StudentTest


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


class StudentTestCreateInput(InputObjectType):
    test = graphene.Int()
    totalPoints = graphene.Int(required=False)


class StudentTestCreateMutation(graphene.Mutation):
    studentTest = graphene.Field(StudentTestType)

    class Arguments:
        input = StudentTestCreateInput(required=True)

    def mutate(self, info, input=None):
        try:
            test = Test.objects.get(id=input.test)
            studentTest = StudentTest(
                user=info.context.user,
                test=test
            )
            studentTest.full_clean()
            studentTest.save()
            return StudentTestCreateMutation(studentTest=studentTest)

        except ValidationError as e:
            return StudentTestCreateMutation(studentTest=None, errors=e)


# StudentTestAnswer
class StudentTestAnswerType(DjangoObjectType):
    class Meta:
        model = StudentTestAnswer


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



# class StudentTestAnswerMutation(SerializerMutation):
#     class Meta:
#         serializer_class = serializers.StudentTestAnswerSerializer
    
#     @classmethod
#     def get_serializer_kwargs(cls, root, info, **input):
#         user = info.context.user
#         requestedUser = User.objects.get(id=input['user'])
#         if user.id != requestedUser.id:
#             raise Exception('Authorization failed')

#         if 'id' in input:
#             test = StudentTest.objects.get(id=input['studentTest'], user=user)
#             instance = StudentTestAnswer.objects.get(id=input['id'], studentTest=test)
#             if instance:
#                 return {'instance': instance, 'data': input, 'partial': True}
#             else:
#                 raise Exception('No such StudentTestAnswer')

#         return {'data': input, 'partial': True}
