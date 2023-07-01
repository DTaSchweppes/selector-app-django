from django.shortcuts import render, redirect
from App.models import SupplierCard
from ..forms import SupplierCardForm


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

def supplier_detail(request, supplier_id):
    if request.method == 'GET':
        supplier_card = SupplierCard.objects.get(id=supplier_id)
        return render(request, 'supcard/supcard.html', {'supplier_card':supplier_card})