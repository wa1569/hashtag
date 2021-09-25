from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog

# Create your views here.
def layout(request):
    return render(request, 'app/layout.html')

def index(request):
    blogs = Blog.objects
    return render(request, 'app/index.html', {'blogs': blogs})

def new(request):
    return render(request, 'app/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/app/index/')

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('index')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'app/new.html', {'form':form})

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('index')

def detail(request, blog_id):
        blog_detail = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'app/detail.html', {'blog':blog_detail})