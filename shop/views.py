from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Slider


# Create your views here.

def index(request):
    slides = Slider.objects.all()
    context = {
        'slides': slides
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
