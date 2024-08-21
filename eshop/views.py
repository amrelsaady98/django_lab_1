from decimal import Decimal

from django.shortcuts import render, redirect

from eshop.models import Product


# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'route': '/home'})

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'route': '/products', 'all_products': all_products})

def add_product_view(request, product_id, is_update):
    print(request.POST)
    if request.method == 'POST':

        product = Product()
        product.name = request.POST.get('name')
        product.price = float(request.POST.get('price'))
        product.description = request.POST.get('description')
        # product = Product(name=name, price=Decimal(price), description=description)
        print(product.name, product.price, product.description)
        product.save()
        # print(name, price, description)

    if is_update:
        product = Product.objects.get(pk=product_id)

    return render(request, 'add_product.html', {'route': '/add_product', 'product': product, 'is_update': is_update})

def edit_product_view(request):
    all_products = Product.objects.all()
    return render(request, 'edit_products.html', {'route': '/edit_products', 'all_products': all_products})

def product_delete_method(request):
    product = Product.objects.get(id=request.GET.get('id'))
    if product is not None:
        product.delete()

    return redirect(edit_product_view)
def product_update_method(request):

    return redirect(add_product_view, id=request.GET.get('id'), is_update=True)
