from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'price',
            'descriptions',
            'stock',
            'get_absolute_url',
            'get_image',
        )