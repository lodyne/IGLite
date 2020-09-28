from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LogoutView
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"You're {username} and you have been created an account. Login now")
            return redirect('login')
    else:
        form=UserRegisterForm()

    context={
        'form':form
    }
    return render (request, 'users/register.html',context)

class MyLogoutView(SuccessMessageMixin ,LogoutView):
    template_name = 'users/logout.html'
    success_message = 'You have been logged out'
    success_url = 'login'
    
