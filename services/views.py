from django.shortcuts import render
from . import views
from .models import Services, Category, Product, Tag, Faaliyet

# Create your views here.

def ServicesView(request):
    services = Services.objects.all().order_by('-date')

    context = {
        'services' : services
    }
    return render(request, 'services/services.html', context)


def Service_Detail_View(request, slug):
    service = Services.objects.get(slug=slug)

    context = {
        'service' : service
    }
    return render(request, 'services/service_detail.html', context)


def ProductsView(request):
    products = Product.objects.all()
    category = Category.objects.all()
    tag =Tag.objects.all()
    faaliyets = Faaliyet.objects.all()

    context = {
        'products' : products,
        'category' : category,
        'tag' : tag,
        'faaliyets' : faaliyets
    }
    return render(request, 'services/products.html', context)


def Product_Detail_View(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product' : product
    }
    return render(request, 'services/product_detail.html', context)


def product_by_category(request, slug):
    products = Product.objects.filter(category__slug=slug)
    category = Category.objects.all()
    tag = Tag.objects.all()
    faaliyets = Faaliyet.objects.all()


    context = {
        'products' : products,
        'category' : category,
        'tag' :tag,
        'faaliyets' : faaliyets
    }
    return render(request, 'services/products.html', context)


def product_by_tag(request, slug):
    products = Product.objects.filter(tag__slug = slug)
    category = Category.objects.all()
    tag = Tag.objects.all()
    faaliyets = Faaliyet.objects.all()


    context = {
        'products' : products,
        'category' : category,
        'tag' : tag,
        'faaliyets' : faaliyets
    }
    return render(request, 'services/products.html', context)


def product_by_faaliyet(request, slug ):
    products = Product.objects.filter(faaliyet__slug = slug)
    category = Category.objects.all()
    tag = Tag.objects.all()
    faaliyets = Faaliyet.objects.all()


    context = {
        'products' : products,
        'category' : category,
        'tag' : tag,
        'faaliyets' : faaliyets
    }
    return render(request, 'services/products.html', context)
