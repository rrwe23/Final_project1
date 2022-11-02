from django.shortcuts import render
from products.models import Product


def index(request,product_pk):
    product = Product.objects.get(id=product_pk)
    reviews = product.review.all()

    context = {
        'reviews' : reviews,

    }
    return render(request,'reviews/index.html',context)




