from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from .models import Jobs, User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserCreationForm,UserProfileForm
from django.shortcuts import get_object_or_404


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
    jobs = Jobs.objects.all().order_by("-last_date")
    return render(request,'Holmes/jobs.html',{"jobs": jobs})
def tempsign(request):
    return render(request,'Holmes/temp_register.html')
def editprofile(request):
    return render(request,'Holmes/edit_profile.html')
def edit_profile(request):
    # user_profile = get_object_or_404(User, pk=pk)
    user_profile = request.user

    if request.method == 'POST':
        print("Request Files - ")
        print(request.FILES)
        print("________________________")
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save()
            
            # user_profile.dp = request.FILES['dp']
            user_profile.save()
        
            print(user_profile.name)
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'Holmes/edit_profile.html', {'form': form})

def applyPage(request,pk):
    job = Jobs.objects.get(pk=pk)
    request.user.jobs_applied.add(job)
    return render(request, 'Holmes/apply_jobs.html',{'job':job})

def status(request):
    user = request.user
    return render(request, 'Holmes/application_status.html',{'user':user})