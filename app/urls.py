from django.urls import path
from .views import addproduct, edit_product_get, productlistview,supplierlistview, addsupplier,deletesupplier,deleteproduct,edit_product_get,edit_product_post,edit_supplier_get,edit_supplier_post, products_filtered, loginview, logout,login_action,logout_action,login
from app import views

urlpatterns = [

    #Landing after login

   # path('landing/', landgingview),

    #Login and logout

    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

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
