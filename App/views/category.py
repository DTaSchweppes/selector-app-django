from django.shortcuts import render, redirect
from App.models import Category
from ..forms import CategoryForm


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/add.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/categories.html', {'categories': categories})
