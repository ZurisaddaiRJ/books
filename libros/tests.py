from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from libros.schema import schema
from libros.models import Libro

LIBROS_QUERY = '''
 {libros { 
    id
    titulo
    autor 
    genero 
    editorial 
    anio 
    numPages 
    costo 
    categoria 
    edicion 
    idioma}}
'''

class LibroTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.libro1 = mixer.blend(Libro)
        self.libro2 = mixer.blend(Libro)

    def test_libros_query(self):
        response = self.query(
            LIBROS_QUERY,
        )


        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query libros results ")
        print (content)
        assert len(content['data']['libros']) == 2