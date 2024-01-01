from django.shortcuts import render, redirect
from Login.models import blog


# Create your views here.

def home(request):
    post_set  = blog.objects.all()
    return render(request, 'Home/home.html', {'blogs':post_set})

def blog_add(request):
    if request.method == 'POST':
        Title = request.POST['title']
        Content = request.POST['content']
        image_file = request.FILES.get('image')
        Video = request.FILES.get('input_video')
        Author = request.POST['author']
        act_blog  = blog(Title=Title, Content=Content, Image=image_file, Author=Author, user = request.user, Video = Video)
        act_blog.save()
        return redirect('/')
    return render(request, 'Home/add.html')

def Myblogs(request):
    current_user = request.user
    mypost = current_user.post_set.all()
    return render(request, 'Home/myblogs.html', {'blogs': mypost})


def profile(request):
    return render(request, 'Home/profile.html')