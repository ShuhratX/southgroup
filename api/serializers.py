from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    big_description = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'image01', 'image02', 'image03', 'image04', 'description', 'big_description')


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(required=False, many=True)
    class Meta:
        model = Category
        fields = ('name','products')


