from django.shortcuts import render, redirect
from App.models import Product
from ..forms import ProductForm


def products_list(request):
    products = Product.objects.all()
    return render(request, 'product/products.html', {"products": products})


def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'product/add.html', {'form': form})