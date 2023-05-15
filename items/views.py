from django.shortcuts import render, get_object_or_404, redirect
from .models import item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm

def detail(request, pk):
    Item = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(category=Item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': Item,
        'related': related_items,
    })
@login_required()
def new(request):
    if (request.method == "POST"):
        form = NewItemForm(request.POST,request.FILES)
        if (form.is_valid()):
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:detail',pk=item.id)
    form = NewItemForm()

    return render(request, 'item/form.html',{
        'form': form
    })