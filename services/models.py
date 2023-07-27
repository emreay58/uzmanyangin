from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/urunler/kategori/{self.slug}/'
    
    
class Tag(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/etiket/{self.slug}/'


class Faaliyet(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextUploadingField()
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/uzman_yangin/faaliyet/{self.slug}/'


class Services(models.Model):
    title =models.CharField(max_length=150)
    image = models.ImageField(upload_to='services/services')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    descriptiondetail = RichTextUploadingField()
    is_home = models.BooleanField(verbose_name='Ana Sayfada Gösterilsin Mi?')
    date = models.DateField(auto_now=True)
    slug = models.SlugField ()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/hizmetler/{self.slug}/'
    

class Product(models.Model):
    title =models.CharField(max_length=150)
    image = models.ImageField(upload_to='services/services')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    faaliyet = models.ManyToManyField(Faaliyet, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    descriptiondetail = RichTextUploadingField()
    date = models.DateField(auto_now=True)
    is_home = models.BooleanField(verbose_name="Ürün Ana Sayfada Gösterilsin Mi?")
    slug = models.SlugField ()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/urunler/{self.slug}/'
    
    