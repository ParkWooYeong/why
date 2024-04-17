from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') or 'products:list')
        messages.error(request,'올바르지 않은 사용자 정보입니다.')
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