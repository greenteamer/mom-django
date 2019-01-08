import graphene

import tests.schema

class Query(tests.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
