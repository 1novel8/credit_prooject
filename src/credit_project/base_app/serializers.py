from rest_framework import serializers
import base_app.models as models


class CreditRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreditRequest
        fields = '__all__'
        read_only_fields = ('date_of_creation', 'is_active')


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contract
        fields = '__all__'
        read_only_fields = ('date_of_creation', 'is_active')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = ('date_of_creation', 'is_active')


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producer
        fields = '__all__'
        read_only_fields = ('date_of_creation', 'is_active')
