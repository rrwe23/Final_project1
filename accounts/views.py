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

            return redirect('products:index')
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

            return redirect(request.GET.get('next') or 'products:index')

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


@login_required
def register_seller(request, user_pk):
    user = get_user_model().objects.get(id=user_pk)
    user.is_seller = True
    user.save()

    return redirect('products:index')


# def naver(request):
#     api_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code'
#     client_ID = '&client_id=xkZnnh3vWdsrFtmARGJW'
#     redirect_uri = parse.quote('http://127.0.0.1:8000/accounts/login/naver/callback')
#     state = parse.quote(f"{request.user}" + f"{random()}")

#     api_url += client_ID
#     api_url += '&redirect_uri=' + redirect_uri
#     api_url += '&state=' + state
    
#     return redirect(api_url)


# def naver_callback(request):
#     api_url = 'https://nid.naver.com/oauth2.0/token?grant_type=authorization_code'
#     client_ID = '&client_id=xkZnnh3vWdsrFtmARGJW'
#     client_secret = '&client_secret=tHkRTl9BWs'
#     code = request.GET.get('code')
#     state = request.GET.get('state')
#     redirect_uri = parse.quote('http://127.0.0.1:8000/accounts/login/naver/callback')

#     api_url += client_ID
#     api_url += client_secret
#     api_url += '&redirect_uri=' + redirect_uri
#     api_url += '&code=' + code
#     api_url += '&state=' + state

#     return redirect(api_url)