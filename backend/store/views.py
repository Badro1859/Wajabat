from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from .models import Product, Category, Store
from .serializers import ProductSerializer, CategorySerializer, StoreSerializer




class ProductViewSet(ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        store = Store.objects.get(pk=request.data['store'])
        if (store.user.id != user.id):
            print('unauthorized reponse')
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().create(request)





class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        products = Product.objects.filter(category=instance)
        context = {'request': request}
        serializer = ProductSerializer(products, many=True, context=context)
        return Response(serializer.data)
    


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer














class LatesProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:15]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_objects(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_objects(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])

def search(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
