from django.shortcuts import render
from .models import Product

def index(request):
    product = Product.objects.order_by("-pk")
    context = {
        "product": product,
    }
    return render(request, "products/index.html", context)




