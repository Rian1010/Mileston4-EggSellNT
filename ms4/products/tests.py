from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    """
    Run against Product models
    """

    def test_str(self):
        test_name = Product(name='This product')
        self.assertEqual(str(test_name), "This product")