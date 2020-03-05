from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
)
class IndexView(TemplateView):
    # que una vista procesa los datos y renderiza el resultado en pantalla
    # siempre nos pedira un template con el trabajar
    # un template es un archivo html
    template_name = "home/index.html"

class ListaLibros(ListView):
    template_name = 'home/lista.html'
    queryset = ['el quijote de la mancha','Codigo limpio',' La somra del viento ','Dejango 2.0']
    context_object_name = 'libros'
