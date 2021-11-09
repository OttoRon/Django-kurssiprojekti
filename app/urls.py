from django.urls import path
from .views import addproduct, edit_product_get, landgingview,productlistview,supplierlistview, addsupplier,deletesupplier,deleteproduct,edit_product_get,edit_product_post,edit_supplier_get,edit_supplier_post, products_filtered
from app import views

urlpatterns = [

    path('', landgingview),
    #Supplier paths
    path('suppliers.html/',supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:iidee>/', deletesupplier),
    path('edit-supplier-get/<int:iidee>/', edit_supplier_get),
    path('edit-supplier-post/<int:iidee>/', edit_supplier_post),

    #path('products/', productlistview),

    #Product paths
    path('products.html/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:iidee>/', deleteproduct),
    path('edit-product-get/<int:iidee>/', edit_product_get),
    path('edit-product-post/<int:iidee>/', edit_product_post),
    path('products-by-supplier/<int:iidee>/', products_filtered),
]
