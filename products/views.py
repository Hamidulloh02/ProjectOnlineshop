from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from.models import Products
from .serializers import ProductSerializer
from .permission import IsAuthorOrReadOnly


#import filter
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter

# Create your views here.

class ProductsAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    # permission_classes = IsAuthorOrReadOnly
    queryset = Products.objects.all()
    serializer_class = ProductSerializer