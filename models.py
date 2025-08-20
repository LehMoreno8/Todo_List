from django.db import models

class ModeloBase(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True),
    modificado_em = models.DateTimeField(auto_now=True)


    class Meta:
       abstract = True

class Grupo(ModeloBase):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'grupo'

class Etiqueta(ModeloBase):
    nome = models.CharField(max_length=256)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'etiqueta'

class Tarefa(ModeloBase):
    nome = models.TextField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    concluido = models.BooleanField(default=False)
    ordem = models.IntegerField(default=0)
    data_vencimento = models.DateField(blank=True, null=True)
    grupo = models.ForeignKey(
        to=Grupo,
        on_delete=models.CASCADE,
        related_name='tarefas',
        blank=True,
        null=True,
        db_column='grupo_id',
    )
    etiquetas = models.ManyToManyField(
        to=Etiqueta,
        related_name='tarefas',
        blank=True,
        db_table='tarefa_etiqueta'
    )


