from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(required=False, many=True)

    class Meta:
        model = Category
        fields = '__all__'
