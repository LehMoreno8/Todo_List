from rest_framework import serializers
from .models import Tarefa, Grupo, Etiqueta


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'


class TarefaSerializer(serializers.ModelSerializer):
     grupo = GrupoSerializer(read_only=True)
    etiquetas = EtiquetaSerializer(many= True, read_only=True)

    grupo_id = serializers.PrimaryKeyRelatedField(
        source='grupo',
        queryset=Grupo.objects.all(),
        write_only=True,
        required=False
    )
    etiquetas_ids = serializers.PrimaryKeyRelatedField(
        source='etiquetas',
        queryset=Etiqueta.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Tarefa
        fields = '__all__'

