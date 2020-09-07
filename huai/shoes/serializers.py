from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import *

class LoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lote
        fields = fields = ['id','nome','dt_fabric','quantidade']

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id','nome','descricao','cor','valor','lote']

class ItemListSerializer(serializers.ModelSerializer):
    lote = LoteSerializer(many=False)

    class Meta:
        model = Item
        fields = ['id','nome','descricao','cor','valor','lote']

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ['id','cpf','nome','dt_nasc']

class VendedorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vendedor
        fields = ['id','username','first_name','last_name','email','last_login']

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = ['id','vendedor','cliente','itens','valor_total','dt_compra']

class PedidoListSerializer(serializers.ModelSerializer):
    vendedor = VendedorSerializer(many=False)
    cliente = ClienteSerializer(many=False)
    itens = ItemListSerializer(many=True)

    class Meta:

        model = Pedido
        fields = ['id','vendedor','cliente','itens','valor_total','dt_compra']

# class CustomRegisterSerializer(RegisterSerializer):
#     vendedor = VendedorSerializer(many=False)

#     def get_cleaned_data(self):
#         super(CustomRegisterSerializer, self).get_cleaned_data()

#         return {
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             'name': self.validated_data.get('name', ''),
#             'vendedor': self.validated_data.get('vendedor', ''),
#         }