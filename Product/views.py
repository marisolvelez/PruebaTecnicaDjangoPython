from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from Product.models import Product
from .serializers.product_serializer import ProductSerializer
from django.core.paginator import Paginator
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import pdb #recordar borrar esto

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#ProductRetrieveUpdateDestroy solo admite métodos GET, PUT, PATCH 
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
        
def crud(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'crud.html', {'page_obj': page_obj})

 
