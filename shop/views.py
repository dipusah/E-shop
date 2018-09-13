from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Slider, Product


# Create your views here.

def index(request):
    slides = Slider.objects.all()
    featured_products = Product.objects.filter(featured=True).all()
    latest_products = Product.objects.order_by('-pub_date')[:5]
    context = {
        'slides': slides,
        'featured_products': featured_products,
        'latest_products': latest_products
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
