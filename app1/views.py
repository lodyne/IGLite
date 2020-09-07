from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def home(request):
    return render(request,'app1/home.html')

def post_list(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'app1/post_list.html',context)

def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post-list')
    else:
        form=PostForm()
        
    context={
        'form':form
    }
    
    return render(request, 'app1/upload_post.html')

def search(request):
    return render(request,'app1/search.html')

def notification(request):
    return render(request,'app1/notification.html')

def message(request):
    return render(request,'app1/message.html')

def profile(request):
    return render(request,'app1/profile.html')