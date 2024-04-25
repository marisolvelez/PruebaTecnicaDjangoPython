from django.urls import path

from .views import ProductListCreate, ProductRetrieveUpdateDestroy
from . import views

urlpatterns = [
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('crud/', views.crud, name='crud')
]
