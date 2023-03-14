import graphene

import libros.schema


class Query(libros.schema.Query, graphene.ObjectType):
    pass

class Mutation(libros.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
