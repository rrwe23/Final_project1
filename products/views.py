from django.shortcuts import render
from .models import Product
from django.contrib.auth import get_user_model


def main(request):
    sellers = get_user_model().objects.filter(is_seller=True)
    context = {
        "sellers": sellers
    }
    return render(request, "products/main.html", context)

    

def index(request, user_pk):
    product = Product.objects.order_by("-pk")
    context = {
        "product": product,
    }
    return render(request, "products/index.html", context)
    


def create(request):
    pass


   
def detail(request):
    pass

def update(request):
    pass

def delete(request):
    pass

def cart(request):
    pass



