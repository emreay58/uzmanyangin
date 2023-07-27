from typing import Union
from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.shortcuts import reverse



class PagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    
    def items(self):
        return('about', 'contact', 'index')
    
    def location(self, item):
        return reverse(item)