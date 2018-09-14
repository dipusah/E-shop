from django.shortcuts import render, redirect
from .forms import SignUpForm, ReviewForm
from .models import Slider, Product, Category


# Create your views here.

def index(request):
    slides = Slider.objects.all()
    featured_products = Product.objects.filter(featured=True).all()
    latest_products = Product.objects.order_by('-pub_date')[:8]
    categories = Category.objects.order_by('title').all()
    context = {
        'slides': slides,
        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories
    }
    return render(request, 'shop/index.html', context)


def test(request):
    return render(request, 'shop/test.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def product(request, product_slug):
    pro = Product.objects.get(slug=product_slug)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = pro
            review.user = request.user
            review.save()

    categories = Category.objects.order_by('title').all()
    context = {
        'product': pro,
        'categories': categories,
        'form': form
    }

    return render(request, 'shop/product.html', context)
