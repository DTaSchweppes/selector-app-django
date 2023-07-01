from django.shortcuts import render, redirect, get_object_or_404
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

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/edit.html', {'form': form, 'product': product})