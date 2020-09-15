from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'insta/home.html',context)

def post_list(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'insta/post_list.html',context)

def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('insta-post_list')
            return redirect('insta-home')
    else:
        form=PostForm()
        
    context={
        'form':form
    }
    
    return render(request, 'insta/upload_post.html',context)

def search(request):
    return render(request,'insta/search.html')

def notification(request):
    return render(request,'insta/notification.html')

def message(request):
    return render(request,'insta/message.html')

def profile(request):
    return render(request,'insta/profile.html')