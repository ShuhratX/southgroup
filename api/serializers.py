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
        fields = ('id', 'title', 'category', 'price', 'image1', 'image2', 'image3', 'image4', 'description', 'big_description')