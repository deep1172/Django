from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ChaiVariety, Store
from .forms import ChaiVarietyForm
# Create your views here.
def all_deep(request):
    deep = ChaiVariety.objects.all()
    return render(request, 'deep/all_deep.html',{'deep': deep})

def deep_detail(request, deep_id):
    deep = get_object_or_404(ChaiVariety, pk=deep_id)
    return render(request, 'deep/deep_detail.html',{'deep': deep})
def services(request):
    return render(request, 'deep/services.html')

def deep_store_view(request):
    stores =None
    if request.method == 'POST':
        form= ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety= form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request, 'deep/deep_stores.html', {'stors': stores, 'form' : form})
  
