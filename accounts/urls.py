from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register_seller/<int:user_pk>', views.register_seller, name='register_seller'),
    path('login/naver/', views.naver, name='naver'),
    path('login/naver/callback', views.naver_callback, name='naver_callback'),
]
