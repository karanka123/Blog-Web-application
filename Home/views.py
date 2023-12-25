from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Home/home.html')

def blog_add(request):
    return render(request, 'Home/add.html')