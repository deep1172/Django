from django.shortcuts import render

# Create your views here.
def all_deep(request):
    return render(request, 'deep/all_deep.html')

def services(request):
    return render(request, 'deep/services.html')


