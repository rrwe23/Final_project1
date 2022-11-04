from django.shortcuts import redirect, render
from products.models import Product
from .forms import ReviewForm
from .models import Review

def index(request, product_pk):
    product = Product.objects.get(id=product_pk)
    reviews = product.review.all()
    form = ReviewForm(instance=product)

    context = {
        'reviews': reviews,
        'product_pk': product_pk,
        'form' : form,
    }
    
    return render(request, 'reviews/index.html', context)


def create(request, product_pk):
    product = Product.objects.get(id=product_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user

            if request.user not in product.review.all():
                review.save()
                product.review.add(review)
            # else:
                # 실패 alert 가 뜨게 만들어야함.

            return redirect('reviews:index', product_pk)

    else:
        form = ReviewForm()

    context = {
        'form': form
    }

    return render(request, 'reviews/forms.html', context)


def update(request, review_pk):
    review = Review.objects.get(id=review_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()

            return redirect('reviews:index', review.review_product.get().id)

    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form
    }

    return render(request, 'reviews/forms.html', context)


def delete(request, review_pk):
    review = Review.objects.get(id=review_pk)
    product_pk = review.review_product.get().id
    review.delete()

    return redirect('reviews:index', product_pk)