from django.contrib import admin

# Register your models here.
from .models import Autor, Libros


# Clase mejorar el administrador de Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    # atributto para buscar un campo
    search_fields = ('nombre','nacionalidad',)

class LibrosAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'resumen',
        'autor',
        'id',
    )
    # atributto para buscar un campo
    search_fields = ('title',)
    #
    list_filter = (
        'autor',
    )
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)


