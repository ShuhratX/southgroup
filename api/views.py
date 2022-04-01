from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer