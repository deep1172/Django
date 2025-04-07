from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, World. You are at the Home page ")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, World. You are at the about page ")
    return render(request, "website/about.html")

def contact(request):
    # return HttpResponse("Hello, World. You are at the contact page ")
    return render(request, 'website/contact.html')

def services(request):
    # return HttpResponse("Hello, World. You are at the services page ")
    return render(request, 'website/services.html')