from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100,verbose_name='Product name')
    price = models.IntegerField(verbose_name="Product price")
    size = models.CharField(max_length=100,verbose_name="Product size")
    body = RichTextField(verbose_name="Product about info")
    poster = models.ImageField(upload_to='images/',blank=True,verbose_name='Products upload image')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Image(models.Model):
    post = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='posterinfo')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
       return f'Images of {self.post.id}'