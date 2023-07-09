from django.shortcuts import render, redirect, get_object_or_404
from App.models import Product
from ..forms import ProductForm
from django.core.paginator import Paginator


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


def shearch_product(request):
    # https://django.fun/ru/docs/django/4.1/ref/contrib/postgres/search/
    query = request.GET.get('query')
    results = Product.objects.filter(name__iregex=query)

    return render(request, 'product/search_results.html', {"results": results})


def products_list(request):
    all_objects = Product.objects.all()
    paginator = Paginator(all_objects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/products.html', {'page_obj': page_obj})
