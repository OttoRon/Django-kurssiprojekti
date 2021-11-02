from django.urls import path
from .views import landgingview,productlistview,supplierlistview, addsupplier
from app import views

urlpatterns = [
    path('', landgingview),
    path('suppliers.html/',supplierlistview),
    path('add-supplier/', addsupplier),
    #path('products/', productlistview),
    path('products.html/', productlistview),
]
