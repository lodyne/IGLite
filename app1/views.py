from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'app1/home.html')

def search(request):
    return render(request,'app1/search.html')

def notification(request):
    return render(request,'app1/notification.html')

def message(request):
    return render(request,'app1/message.html')

def profile(request):
    return render(request,'app1/profile.html')