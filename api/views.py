from django.http import HttpResponse
from django.views import View


class ProductView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

    def post(self, request):
        # <view logic>
        return HttpResponse('result')
