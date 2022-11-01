from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('accounts/', include('accounts.urls')),
    # path('products/', include('products.urls')),
    # path('reviews/', include('reviews.urls')),
]
