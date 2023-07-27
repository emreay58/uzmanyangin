from django.shortcuts import render
from services.models import Services, Product


# Create your views here.

def IndexView(request):
    services = Services.objects.filter(is_home=True).order_by('-date')
    products = Product.objects.filter(is_home=True).order_by('-date')

    context = {
        'services' : services,
        'products' : products
    }
    return render(request, 'pages/index.html', context)


def AboutView(request):
    return render(request, 'pages/about.html')


def ContactView(request):
    return render(request, 'pages/contact.html')