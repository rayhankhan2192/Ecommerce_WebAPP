from django.shortcuts import render

from .serializers import ProductGetSerializers, ProductSerializers
from category.serializers import CategorySerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from .models import Product
from rest_framework import status


class ProductsListView(APIView):
    def get(self, request, format = None):
        products = Product.objects.all()
        serializer = ProductGetSerializers(products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailsView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug = category_slug).get(slug = product_slug)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, category_slug, product_slug, format = None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductGetSerializers(product)
        return Response(serializer.data)
        