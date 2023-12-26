from django.shortcuts import render, redirect
from Login.models import blog


# Create your views here.

def home(request):
    return render(request, 'Home/home.html', {'blogs':blog.objects.all()})

def blog_add(request):
    if request.method == 'POST':
        Title = request.POST['title']
        Content = request.POST['content']
        Image= request.POST['image']
        Video = request.POST['input_video']
        Author = request.POST['author']
        act_blog  = blog(Title=Title, Content=Content, Image=Image, Author=Author, user = request.user)
        act_blog.save()
        return redirect('/')
    return render(request, 'Home/add.html')

def Myblogs(request):
    return 