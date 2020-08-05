from django.urls import path

from api.views import ProductView

urlpatterns = [
    path('products', ProductView.as_view(), name='product'),
]
