from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.models import User
from django.template import loader
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def homepage(request):
    return render(request, 'indexpage.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def userlist(request):
    user_list = User.objects.all()
    context= {'user_list':user_list}
    return render(request, 'userpage.html',context)

def userdetails(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'user':user,
    }
    return render(request, 'detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, your account is created")
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signuppage.html', {'form' : form})

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'blogcontent.html',context)

def blogpage(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request,'blogpage.html',context)