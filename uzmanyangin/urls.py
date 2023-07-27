
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import PagesSitemap
from services.sitemaps import ProductSitemap, ServiceSitemap,  CategorySitemap, TagSitemap, FaaliyetSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'pages' : PagesSitemap,
    'services' : ServiceSitemap,
    'products' : ProductSitemap,
    'categories' : CategorySitemap,
    'tags' : TagSitemap,
    'faaliyets' : FaaliyetSitemap 
}

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('services.urls')),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

