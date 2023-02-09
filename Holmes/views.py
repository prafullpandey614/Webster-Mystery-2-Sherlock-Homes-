from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserCreationForm

def index(request):
    if request.user.is_authenticated:
        return render(request,'Holmes/home_page.html',{'user': request.user})
    return render(request, 'Holmes/home_page.html')

def account_page(request,username):
    user = User.objects.get(username=username)
    return render(request, 'Holmes/account_page.html',{"user":user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Holmes/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'Holmes/login.html')
def profile(request):
    user = request.user
    return render(request,'Holmes/profile.html',{"user": user})
def jobs(request):
    return render(request,'Holmes/jobs.html')