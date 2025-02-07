from rest_framework import serializers
from .models import Customer, CarPart, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'address', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Customer.objects.create_user(**validated_data)
        return user

class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPart
        fields = ['id', 'part_number', 'name', 'description', 'price', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'part', 'quantity', 'created_at']
        read_only_fields = ['customer', 'created_at']
