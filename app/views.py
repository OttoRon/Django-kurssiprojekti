from django.shortcuts import render
from django.shortcuts import redirect
from .models import Supplier, Product

def landgingview(request):
        return render(request, "landingpage.html")

#SUPPLIERS HANDLING

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

def edit_supplier_get(request,iidee):
        supplier = Supplier.objects.filter(id = iidee)
        context = {'supplier': supplier}
        return render (request, "edit_supplier.html",context)

def edit_supplier_post(request,iidee):
        item = Supplier.objects.get(id = iidee)
        item.address = request.POST['address']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.save()
        return redirect(supplierlistview)         
         
            

#PRODUCTS HANDLING


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

def edit_product_get(request,iidee):
        product = Product.objects.filter(id = iidee)
        context = {'product': product}
        return render (request, "edit_product.html",context)

def edit_product_post(request,iidee):
        item = Product.objects.get(id = iidee)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)                     