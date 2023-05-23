import graphene

import libros.schema
import users.schema
import graphene
import graphql_jwt


class Query(users.schema.Query, libros.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, libros.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
