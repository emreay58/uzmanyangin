from typing import Union
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Product, Services,Category,Tag,Faaliyet


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.all()
    
    
class ServiceSitemap(Sitemap):

    def items(self):
        return Services.objects.all()
    

class CategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()
    

class TagSitemap(Sitemap):

    def items(self):
        return Tag.objects.all()
    

class FaaliyetSitemap(Sitemap):

    def items(self):
        return Faaliyet.objects.all()