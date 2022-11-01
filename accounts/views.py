from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # user = form.save()
            # auth_login(request, user)

            return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)