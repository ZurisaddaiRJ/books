import graphene
from graphene_django import DjangoObjectType

from .models import Libro
from users.schema import UserType
from libros.models import Libro, Vote
from graphql import GraphQLError
from django.db.models import Q


class LibroType(DjangoObjectType):
    class Meta:
        model = Libro

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    libros = graphene.List(LibroType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_libros(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(titulo__icontains=search) |
                Q(genero__icontains=search)
            )
            return Libro.objects.filter(filter)
        return Libro.objects.all()
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    

class CreateLibro(graphene.Mutation): #VARIABLES DE LA CLASE
    id = graphene.Int() #EL ID SE GENERA SOLO
    titulo = graphene.String()
    autor = graphene.String()
    genero = graphene.String()
    editorial = graphene.String()
    anio = graphene.Int()
    num_pages = graphene.Int()
    costo = graphene.Int()
    categoria = graphene.String()
    edicion = graphene.Int()
    idioma = graphene.String()
    posted_by = graphene.Field(UserType)


    #2
    class Arguments: #Parametros que se van a la API
        titulo = graphene.String()
        autor = graphene.String()
        genero = graphene.String()
        editorial = graphene.String()
        anio = graphene.Int()
        num_pages = graphene.Int()
        costo = graphene.Int()
        categoria = graphene.String()
        edicion = graphene.Int()
        idioma = graphene.String()

    #3
    def mutate(self, info, titulo,autor, genero, editorial,anio,num_pages,costo,categoria,edicion,idioma): #El parametro info y self son obligatorios
        user = info.context.user or None 
        libros = Libro(titulo=titulo,
                       autor=autor, 
                       genero=genero,
                       editorial=editorial,
                       anio=anio,
                       num_pages=num_pages,
                       costo=costo,
                       categoria=categoria,
                       edicion=edicion,
                       posted_by=user,
                       idioma=idioma) #Programación Orientada a Objetos. LLENAR EL OBJETO.
        libros.save() #INSERT INTO Libro (....) values (....)

        return CreateLibro(
            id=libros.id,  #CUANDO HACEMOS UN POST ES IMPORTANTE SABER QUE ID GENERO
            titulo=libros.titulo,
            autor=libros.autor,
            genero=libros.genero,
            editorial=libros.editorial,
            anio=libros.anio,
            num_pages=libros.num_pages,
            costo=libros.costo,
            categoria=libros.categoria,
            edicion=libros.edicion,
            posted_by=libros.posted_by,
            idioma=libros.idioma,

        )
    

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    book = graphene.Field(LibroType)

    class Arguments:
        book_id = graphene.Int()

    def mutate(self, info, book_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        book = Libro.objects.filter(id=book_id).first()
        if not book:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            book=book,
        )

        return CreateVote(user=user, book=book)


#4
class Mutation(graphene.ObjectType):
    create_libros = CreateLibro.Field()
    create_vote = CreateVote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)