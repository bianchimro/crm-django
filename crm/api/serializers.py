from rest_framework.serializers import ModelSerializer
from base.models import Azienda, Persona


class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"


class AziendaSerializer(ModelSerializer):
    persone = PersonaSerializer(many=True, read_only=True)
    class Meta:
        model = Azienda
        fields = "__all__"
