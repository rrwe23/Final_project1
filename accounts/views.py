from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # user = form.save()
            # auth_login(request, user)

            # 수정 필요
            return redirect('accounts:signup')
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

            # 수정 필요
            return redirect(request.GET.get('next') or 'accounts:signup')

    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)