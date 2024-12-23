from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form})


def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'delete_item.html', {'item': item})
