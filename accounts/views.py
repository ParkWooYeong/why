from django.shortcuts import render, redirect, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from accounts.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') or 'products:list')
        messages.error(request,'이게 맞을까요?')
    return render(request,'accounts/login.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect("products:list")



def signup_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products:list')
    
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html', context)

def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/profile.html', {'profile_user': user})

@login_required
@require_POST
def follow_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.followers.filter(id=request.user.id).exists():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile', user_id=user_id)