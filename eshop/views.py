from decimal import Decimal

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from eshop.forms import LoginForm, RegisterForm
from eshop.models import Product


# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'route': '/home'})


def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'route': '/products', 'all_products': all_products})


def add_product_view(request):
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

    return render(request, 'add_product.html', {'route': '/add_product'})


def edit_product_view(request):
    all_products = Product.objects.all()
    return render(request, 'edit_products.html', {'route': '/edit_products', 'all_products': all_products})


def product_delete_method(request):
    product = Product.objects.get(id=request.GET.get('id'))
    if product is not None:
        product.delete()

    return redirect(edit_product_view)


def product_update_method(request):
    product = Product.objects.get(id=request.GET.get('id'))
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = float(request.POST.get('price'))
        product.description = request.POST.get('description')
        product.save()
        return redirect(edit_product_view)
    return render(request, 'edit_form.html', {'route': '/edit_products', 'product': product})


# def login_view(request):
#     # TODO: implement login POST method business logic
#     return render(request, 'login-form.html', {'route': '/login'})


def register_view(request):
    error_message = ''
    if  request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            if cd['password'] == cd['re_password']:
                user = User.objects.create_user(
                    username=cd['username'],
                    password=cd['password']
                )
                login(request, user)
                return redirect(home_view)
            else:
                error_message = 'Passwords do not match'

    form = RegisterForm()
    return render(request, 'register-form.html', {'route': '/register', 'form': form, 'error_message': error_message})


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                login(request, user)
                return redirect(home_view)
            else:
                error_message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'login-form.html', {'route': '/login', 'form': form, 'error_message': error_message})
