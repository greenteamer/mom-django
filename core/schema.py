import graphene

import tests.schema

class Query(
    tests.schema.TestQuery,
    tests.schema.TestQuestionQuery,
    tests.schema.TestQuestionVariantQuery,
    tests.schema.StudentTestQuery,
    tests.schema.StudentTestAnswerQuery,
    graphene.ObjectType):
    pass

class Mutations(graphene.ObjectType):
    create_student_test = tests.schema.StudentTestCreateMutation.Field()
    # update_student_test = tests.schema.StudentTestMutation.Field()

    create_student_test_answer = tests.schema.StudentTestAnswerMutation.Field()
    update_student_test_answer = tests.schema.StudentTestAnswerMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
