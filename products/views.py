from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import get_user_model
from .forms import ProductForm


def main(request):
    sellers = get_user_model().objects.filter(is_seller=True)
    products = Product.objects.all()
    context = {
        "sellers": sellers,
        "products": products
    }
    return render(request, "products/main.html", context)

    

def index(request, user_pk):
    products = Product.objects.order_by("-pk")
    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)
    


def create(request, user_pk):
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products:index', user_pk)
    else:
        product_form = ProductForm()
    context = {
        "product_form": product_form
    }
    return render(request, "products/forms.html", context)


   
def detail(request, user_pk, product_pk):
    product = Product.objects.get(pk=product_pk)
    context = {
        "product":product
    }
    return render(request, "products/detail.html", context, user_pk)
    

def update(request):
    pass

def delete(request):
    pass

def cart(request):
    pass



