from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ChaiVariety

# Create your views here.
def all_deep(request):
    deep = ChaiVariety.objects.all()
    return render(request, 'deep/all_deep.html',{'deep': deep})

def deep_detail(request, deep_id):
    deep = get_object_or_404(ChaiVariety, pk=deep_id)
    return render(request, 'deep/deep_detail.html',{'deep': deep})
def services(request):
    return render(request, 'deep/services.html')


