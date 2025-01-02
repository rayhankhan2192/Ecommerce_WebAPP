from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'slug',
            'price',
            'images',
            'descriptions',
            'stock',
            'is_available',
            'category',
            'get_absolute_url',
            'get_image',
            'create_date',
            'modified_at'
        )

class ProductGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'price',
            'descriptions',
            'stock',
            'is_available',
            'category',
            'get_absolute_url',
            'get_image',
        )