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
CREATE_LIBROS_MUTATION = '''
mutation createLibroMutation($titulo: String, $autor: String, $genero: String, $editorial: String, $anio: Int, $numPages: Int, $costo: Int, $categoria: String, $edicion: Int, $idioma: String){
 createLibros(titulo: $titulo, autor: $autor, genero: $genero, editorial: $editorial, anio: $anio, numPages: $numPages, costo: $costo, categoria: $categoria, edicion: $edicion, idioma: $idioma){
  titulo
  autor
  genero
  editorial
  anio
  numPages
  costo
  categoria
  edicion
  idioma

 }
}
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

    def test_createLibro_mutation(self):

        response = self.query(
            CREATE_LIBROS_MUTATION,
            variables={'titulo': 'Todo lo que nunca fuimos', 'autor': 'Alice Kellen', 'genero': 'Novela rosa, Ficción', 'editorial': 'Planeta', 'anio': 2019, 'numPages': 352, 'costo': 398, 'categoria': 'Juvenil', 'edicion': 2, 'idioma': 'Español'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createLibros": {"titulo": "Todo lo que nunca fuimos", 'autor': 'Alice Kellen', 'genero': 'Novela rosa, Ficción', 'editorial': 'Planeta', 'anio': 2019, 'numPages': 352, 'costo': 398, 'categoria': 'Juvenil', 'edicion': 2, 'idioma': 'Español'}}, content['data'])
