from rest_framework import serializers
from .models import Category
from product.serializers import ProductSerializers
from product.models import Product

class CategorySerializers(serializers.ModelSerializer):
    products = ProductSerializers(many = True)
    class Meta:
        model = Category
        fields = (
            'id',
            'category_name',
            'get_absolute_url',
            'products',
        )
        