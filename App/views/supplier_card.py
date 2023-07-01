from django.shortcuts import render, redirect
from App.models import SupplierCard
from ..forms import SupplierCardForm

def home(request):
    from django.db import connection

    table_names = connection.introspection.table_names()
    print(table_names)
    result = SupplierCard.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'supplier_cards': result})

def supplier_card_list(request):
    supplier_cards = SupplierCard.objects.all()
    return render(request, 'supcard/sup_cards.html', {'supplier_cards': supplier_cards})


def add_supplier_card(request):
    if request.method == 'POST':
        form = SupplierCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_card_list')
    else:
        form = SupplierCardForm()
    return render(request, 'supcard/add.html', {'form': form})
