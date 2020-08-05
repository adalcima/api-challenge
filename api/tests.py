from django.test import RequestFactory, TestCase

from api.models import Product
from api.views import ProductView


class ProductViewTestCase(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.product = Product.objects.create(
            id='123',
            name='test_product',
            value=2.5,
            discount_value=1.5,
            stock=2,
        )

    def test_list_products(self):
        request = self.request_factory.get('api/v1/products')

        response = ProductView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_create_products(self):
        request = self.request_factory.post('api/v1/products')
        product = Product(
            id='456',
            name='new_product',
            value=4.8,
            discount_value=3.8,
            stock=5,
        )

        response = ProductView.as_view()(request)
        self.assertEqual(response.status_code, 200)
