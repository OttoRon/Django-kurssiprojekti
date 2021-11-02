from django.urls import path
from .views import addproduct, edit_product_get, landgingview,productlistview,supplierlistview, addsupplier,deletesupplier,deleteproduct,edit_product_get,edit_product_post
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
    path('edit-product-get/<int:iidee>/', edit_product_get),
    path('edit-product-post/<int:iidee>/', edit_product_post),
]
