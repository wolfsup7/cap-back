from rest_framework import generics
from .serializers import ClientSerializer
from .models import Client


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer
