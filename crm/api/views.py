from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from base.models import Azienda
from api.serializers import AziendaSerializer


class ExampleView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({"ciao":"ruben"})


class AziendaList(generics.ListAPIView):
    queryset = Azienda.objects.all()
    serializer_class = AziendaSerializer


class AziendaViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Azienda.objects.all()
    serializer_class = AziendaSerializer
