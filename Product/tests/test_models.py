from django.test import TestCase
from ..models import Product
from django.db.models.fields.files import ImageFieldFile

class ProductModelTestCase(TestCase):
    def setUp(self):
        # Crea objetos de prueba si es necesario
        Product.objects.create(name_product="Test Name", description="Test Description", price=20.00, stock=100, image="http://127.0.0.1:8000/media/product_images/c252868448718381ac5f29d467573e10.jpg")

    def test_model_creation(self):
        # Obtén un objeto de la base de datos
        obj = Product.objects.get(name_product="Test Name")
        # Asegúrate de que se haya creado correctamente
        self.assertEqual(obj.name_product, "Test Name")
        self.assertEqual(obj.description, "Test Description")
        self.assertEqual(obj.price, 20.00)
        self.assertEqual(obj.stock, 100)
        self.assertEqual(obj.image, "http://127.0.0.1:8000/media/product_images/c252868448718381ac5f29d467573e10.jpg")

class ProductModelTestCases(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name_product='Camisa',
            description='Camisa de algodón',
            price=20.00,
            stock=100,
            image = 'path/to/your/image.jpg'
        )
    
    def test_product_name_type(self):
        self.assertIsInstance(self.product.name_product, str)

    def test_product_description_type(self):
        self.assertIsInstance(self.product.description, str)

    def test_product_price_type(self):
        self.assertIsInstance(self.product.price, float)

    def test_product_stock_type(self):
        self.assertIsInstance(self.product.stock, int)
    
    def test_product_image_type(self):
        self.assertIsInstance(self.product.image, ImageFieldFile)
