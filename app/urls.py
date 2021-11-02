from django.urls import path
from .views import landgingview,productlistview,supplierlistview
from app import views

urlpatterns = [
    path('', landgingview),
    path('suppliers.html/',supplierlistview),
    #path('products/', productlistview),
    path('products.html/', productlistview),
]
