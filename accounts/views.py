from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # user = form.save()
            # auth_login(request, user)

            return redirect('products:main')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            return redirect(request.GET.get('next') or 'products:main')

    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)

    return redirect('accounts:login')


@login_required
def profile(request):
    
    return render(request, 'accounts/profile.html')