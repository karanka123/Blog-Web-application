from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Home/home.html')

def blog_add(request):
    if request.method == 'POST':
        Title = request.POST['title']
        Content = request.POST['content']
        Image= request.POST['image']
        Video = request.POST['input_video']
        return render(request, 'Home/home.html',{'Header':Title,
                                'Content': Content,
                                'Image': Image,
                                'Video': Video})
    return render(request, 'Home/add.html')