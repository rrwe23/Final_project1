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
    products = Product.objects.filter(user_id=user_pk)
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


def detail(request, product_pk):
    # seller = get_user_model().objects.get(id=user_pk)
    product = Product.objects.get(id=product_pk)
    context = {
        "product":product
    }
    return render(request, "products/detail.html", context)
    

def update(request, product_pk):
    product = Product.objects.get(id=product_pk)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect("products:detail", product_pk)
    else:
        product_form = ProductForm(instance=product)
    context = {
        "product_form": product_form
    }
    return render(request, "products/forms.html", context)

def delete(request, product_pk):
    product = Product.objects.get(id=product_pk)
    user_id = product.user_id
    product.delete()
    return redirect("products:index", user_id)


def add_cart(request, product_pk):
    product = Product.objects.get(id=product_pk)

    if request.user in product.cart.all():
        product.cart.remove(request.user)
    else:
        product.cart.add(request.user)
        
    return redirect('products:detail', product_pk)


def show_cart(request, user_pk):
    user = get_user_model().objects.get(id=user_pk)
    cart = user.cart_product.all()
    
    context = {
        'cart': cart
    }

    return render(request, 'products/wishlist.html', context)



