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
