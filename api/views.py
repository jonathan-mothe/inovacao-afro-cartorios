from django.shortcuts import render
from rest_framework import viewsets, generics
from api.models import Estado, Cartorios
from api.serializers import EstadoSerializer, CartoriosSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CartoriosViewSet(viewsets.ModelViewSet):
    queryset = Cartorios.objects.all()
    serializer_class = CartoriosSerializer
    

class CartorioUfList(generics.ListAPIView):
    serializer_class = CartoriosSerializer

    def get_queryset(self):
        uf = self.kwargs['uf']
        #print(self.kwargs)
        return Cartorios.objects.filter(uf=uf)
