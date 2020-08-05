from django.http import JsonResponse
from django.views import View

from api.models import Product
from api.validators import get_product_error


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        results = []

        for product in products:
            obj = {
                'id': product.id,
                'name': product.name,
                'value': product.value,
                'discount_value': product.discount_value,
                'stock': product.stock,
            }
            results.append(obj)

        return JsonResponse({'product': results})

    def post(self, request):
        product_data = request.POST
        total_errors = 0
        product_report = []

        for product in product_data:
            new_product = Product(
                id=product.get('id'),
                name=product.get('name'),
                value=product.get('value'),
                discount_value=product.get('discount_value'),
                stock=product.get('stock'),
            )

            errors = get_product_error(new_product)
            if errors:
                total_errors += 1
                product_report.append({'product_id': id, 'errors': errors})

            else:
                new_product.save()

        response = {'status': 'OK'}
        if total_errors:
            response = {
                'status': 'ERROR',
                'products_report': product_report,
                'number_of_products_unable_to_parse': total_errors,
            }

        return JsonResponse(response)
