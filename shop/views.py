from django.shortcuts import render, redirect
from .forms import SignUpForm


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


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
