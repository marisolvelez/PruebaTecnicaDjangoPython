from ..models import Product
from rest_framework.test import APITestCase
from rest_framework import status
import json

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.product_data = {
            'name_product': 'Camisa',
            'description': 'Camisa de algodón',
            'price': 25.06,
            'stock': 100
        }

    def test_create_product(self):
        json_data = json.dumps(self.product_data)
        response = self.client.post('/product/api/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
