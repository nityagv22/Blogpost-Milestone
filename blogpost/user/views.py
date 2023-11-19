from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.template import loader
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request, 'indexpage.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def userlist(request):
    user_list = Users.objects.all()
    template = loader.get_template("userpage.html")
    context= {'user_list':user_list,}
    return render(request, 'userpage.html',context)

def userdetails(request, user_id):
    user = Users.objects.get(pk=user_id)
    context = {
        'user':user,
    }
    return render(request, 'detail.html', context)

def signup(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('user_name')
        messages.success(request,f"Hello {username}, your account is created")
        return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'signuppage.html',context)