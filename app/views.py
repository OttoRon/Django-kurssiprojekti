from django.shortcuts import render

from EkaDjangoProjekti.app.models import Supplier
from .models import Supplier, Product

def landgingview(request):
    return render(request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request, "suppliers.html", context)

def productslistview(request):
    productslist = Product.objects.all()
    context = {'product': productslist}
    return render (request, "products.html", context)

