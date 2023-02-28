import graphene

import libros.schema


class Query(libros.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
