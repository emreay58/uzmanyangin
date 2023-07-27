from django.urls import path
from . import views

urlpatterns = [
    path('hizmetler/', views.ServicesView, name='services'),
    path('hizmetler/<slug:slug>/', views.Service_Detail_View, name='service_detail'),
    path('urunler/', views.ProductsView, name='products'),
    path('urunler/<slug:slug>/', views.Product_Detail_View, name='product_detail'),
    path('urunler/kategori/<slug:slug>/', views.product_by_category, name='product_by_category'),
    path('etiket/<slug:slug>/', views.product_by_tag, name='product_by_tag'),
    path('uzman_yangin/faaliyet/<slug:slug>/', views.product_by_faaliyet, name='product_by_faaliyet'),
]
