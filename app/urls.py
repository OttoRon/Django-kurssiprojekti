from django.urls import path
from .views import addproduct, landgingview,productlistview,supplierlistview, addsupplier,deletesupplier,deleteproduct
from app import views

urlpatterns = [
    path('', landgingview),
    path('suppliers.html/',supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:iidee>/', deletesupplier),
    #path('products/', productlistview),
    path('products.html/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:iidee>/', deleteproduct),
]
