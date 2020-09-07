# from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
class LoteListCreate(generics.ListCreateAPIView):

    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    permission_classes = (IsAuthenticated,)

class LoteDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    permission_classes = (IsAuthenticated,)

class ItemList(generics.ListAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = (IsAuthenticated,)

class ItemListCreate(generics.ListCreateAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)


class ClienteListCreate(generics.ListCreateAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)


class VendedorList(generics.ListAPIView):

    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = (IsAuthenticated,)

class PedidoList(generics.ListAPIView):

    queryset = Pedido.objects.all()
    serializer_class = PedidoListSerializer
    permission_classes = (IsAuthenticated,)

class PedidoListCreate(generics.ListCreateAPIView):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)

class PedidoRelatorio(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['valor_total', 'dt_compra']
    