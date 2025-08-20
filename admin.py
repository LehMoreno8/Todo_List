from django.contrib import admin

from tasks import models


@admin.register(models.Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criado_em', 'modificado_em')
    # search_fields = ('nome', 'descricao')
    # list_filter = ('criado_em', 'modificado_em')

@admin.register(models.Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    # search_fields = ('nome', 'descricao')

@admin.register(models.Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'concluido', 'ordem', 'data_vencimento')
    # search_fields = ('nome', 'descricao')
    # list_filter = ('criado_em', 'modificado_em')



# Register your models here.
