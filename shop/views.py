from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def test(request):
    return render(request, 'shop/test.html')


def register(request):
    form = SignUpForm()
    context = {'form': SignUpForm}
    return render(request, 'registration/register.html', context)
