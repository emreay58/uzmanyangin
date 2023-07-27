from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('hakkimizda/', views.AboutView, name='about'),
    path('iletisim/', views.ContactView, name='contact'),
]
