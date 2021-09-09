from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from home import  urls
from django.urls import reverse
#from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        tel = request.POST['tel']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already registered')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.profile.tel=tel
                user.save();
                return redirect('/login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('/register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('hi')
            return redirect('/')
        else:
            messages.info(request, 'Credentials are invalid')
            print('hello')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    text=request.POST['text']
    amount_of_words=len(text.split())
    print(amount_of_words)
    return render(request, 'counter.html', {'amount': amount_of_words})

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

<<<<<<< HEAD
def add_widget(request):
    pass
=======
def signup(request):
    return render(request, "signup.html", {})

def forgotpassword(request):
    return render(request, "forgotpassword.html", {})    
>>>>>>> 3b72833707a677eeabf54d3a4c40c857aa8a9b47
