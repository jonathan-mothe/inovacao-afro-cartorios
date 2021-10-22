from rest_framework import serializers
from api.models import Estado, Cartorios


class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estado
        fields = '__all__'


class CartoriosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cartorios
        fields = '__all__'
