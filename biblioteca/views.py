from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
)
from .models import Autor, Libros
class ListaAutores(ListView):
    template_name = 'biblioteca/lista-autores.html'
    model = Autor
    context_object_name = 'autores'

class ListaLibrosAutores(ListView):
    """ Vista para listar libros por autor    """
    template_name = 'biblioteca/lista-libros.html'
    model = Libros
    context_object_name = 'Libros'

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs['pk']
        # filtro de los libros
        lista = Libros.objects.filter(
            autor=id
        )
        #devulevo el resultado
        return lista

