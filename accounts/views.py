from django.shortcuts import render,get_object_or_404
from .forms import UserRegistrationForm,LoginForm
from .models import User
from web.models import Product, Category
from django.http import HttpResponse
from .functions import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import Q
from django.shortcuts import redirect
from django.conf import settings

def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      cd = user_form.cleaned_data
      
      # Create a new user object but avoid saving yet
      new_user = user_form.save(commit=False)
      # set the chosen password
      new_user.set_password(cd['password'])
      #save the user  objects
      new_user.save()
      request.session['first_name'] = new_user.first_name
      #print('new user first name',new_user.first_name)
      
      return redirect('accounts:register_complete')
    else:
        print(user_form.errors)

  else:
    user_form = UserRegistrationForm()
  return render(request, "accounts/register.html",{'user_form':user_form}) 


def register_complete(request):
    return render(request,'accounts/register-complete.html',{'username':request.session.get('first_name')})



def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username',username)
        print('password',password)
        if login_form.is_valid():
            user = authenticate(request,username=username , password=password)
            if user is not None:
                auth_login(request,user)
                next_url = request.GET.get('next')
                print('next_url ========> ',next_url)
                if next_url is not None:
                  url = settings.BASE_URL + next_url
                  print("Final Url ===> ",url)
                else:
                  url = "web:dashboard"
                return redirect(url)
            else:
                return HttpResponse("You Entered wrong password")
        else:
            print(login_form.errors)
    else:
        login_form = LoginForm()
    return render(request,'accounts/login.html',{'login_form':login_form})

def user_logout(request):
    auth_logout(request)
    return redirect('web:home')
    return HttpResponse("Now you are logged out")




