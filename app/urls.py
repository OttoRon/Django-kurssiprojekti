from django.urls import path
from .views import landgingview,productlistview,supplierlistview

urlpatterns = [
    path('', landgingview),
    path('suppliers/', supplierlistview),
    path('products/', productlistview),
]
