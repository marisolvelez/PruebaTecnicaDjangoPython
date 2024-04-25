from rest_framework import serializers
from Product.models import Product # type: ignore

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'name_product', 'description', 'price', 'stock', 'image']