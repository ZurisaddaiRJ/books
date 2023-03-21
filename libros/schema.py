import graphene
from graphene_django import DjangoObjectType

from .models import Libro


class LibroType(DjangoObjectType):
    class Meta:
        model = Libro


class Query(graphene.ObjectType):
    libros = graphene.List(LibroType)

    def resolve_libros(self, info, **kwargs):
        return Libro.objects.all()
    

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
        libros = Libro(titulo=titulo,
                       autor=autor, 
                       genero=genero,
                       editorial=editorial,
                       anio=anio,
                       num_pages=num_pages,
                       costo=costo,
                       categoria=categoria,
                       edicion=edicion,
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
            idioma=libros.idioma,
        )


#4
class Mutation(graphene.ObjectType):
    create_libros = CreateLibro.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)