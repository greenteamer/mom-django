import graphene

import tests.schema
import tests.answers.schema
import profiles.schema


class Query(
    profiles.schema.UserQuery,
    tests.schema.TestQuery,
    tests.schema.TestQuestionQuery,
    tests.schema.TestQuestionVariantQuery,
    tests.answers.schema.StudentTestQuery,
    tests.answers.schema.StudentTestAnswerQuery,
    graphene.ObjectType):
    pass

class Mutations(graphene.ObjectType):
    create_student_test = tests.answers.schema.StudentTestCreateMutation.Field()
    # update_student_test = tests.schema.StudentTestMutation.Field()

    # create_student_test_answer = tests.schema.StudentTestAnswerMutation.Field()
    # update_student_test_answer = tests.schema.StudentTestAnswerMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
