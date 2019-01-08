import graphene

import tests.schema

class Query(tests.schema.Query, graphene.ObjectType):
    pass

class Mutations(graphene.ObjectType):
    # create_student_test = tests.schema.StudentTestMutation.Field()
    create_student_test = tests.schema.CreateStudentTestMutation.Field()
    # update_student_test = tests.schema.StudentTestMutation.Field()

    create_student_test_answer = tests.schema.StudentTestAnswerMutation.Field()
    update_student_test_answer = tests.schema.StudentTestAnswerMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
