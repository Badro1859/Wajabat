from rest_framework import serializers


from .models import Category, Product, Store

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.name')
    
    class Meta:
        model = Product
        fields = (
            "url",
            "id",
            "name",
            "description",
            "price",
            'category',
            'store'
        )
        

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    products = ProductSerializer(many=True)

    class Meta:
        model = Store
        fields = (
            "url",
            "id",
            "name",
            "owner",
            "products"
        )

    




class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # products = ProductSerializer(many=True)
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "products"
        )