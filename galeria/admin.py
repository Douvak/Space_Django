from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

class Listarfotografias(admin.ModelAdmin):
    list_display = ('id','nome','legenda', 'publicado')
    list_display_links = ('nome','id')
    search_fields = ('nome', 'id',)
    list_editable = ('publicado',)
    list_filter = ('categoria',)
    list_per_page = 10
    
admin.site.register(Fotografia, Listarfotografias)

