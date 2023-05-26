from rest_framework import serializers

from products.models import Products,Image


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id', 'post', 'image'
        )


class ProductSerializer(serializers.ModelSerializer):
    posterinfo = PostImagesSerializer(many=True)
    class Meta:
        model = Products
        fields = ('id','name','price','body','size','poster','posterinfo','created_at')