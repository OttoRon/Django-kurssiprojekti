from django.shortcuts import render
from django.shortcuts import redirect
from .models import Supplier, Product

def landgingview(request):
        return render(request, "landingpage.html")

def supplierlistview(request):
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request, "suppliers.html", context)

def addsupplier(request):
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request,iidee):
         Supplier.objects.filter(id = iidee).delete()
         return redirect(request.META['HTTP_REFERER'])       
...

def productlistview(request):
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render (request,"products.html",context)


def addproduct(request):
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])
      
def deleteproduct(request,iidee):
         Product.objects.filter(id = iidee).delete()
         return redirect(request.META['HTTP_REFERER']) 