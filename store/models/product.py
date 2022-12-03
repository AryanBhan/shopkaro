from distutils.command.upload import upload
from email.policy import default
from os import stat
from unicodedata import category

from django.db import models

from .category import Category

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    desc=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='upload/products/')
    def __str__(self) -> str:
        return self.name
    @staticmethod
    def get_all_product():
        return Product.objects.all()
    @staticmethod
    def get_product_by_list(id):
        return Product.objects.filter(id__in=id)
    @staticmethod
    def get_all_product_by_catid(category_id):
        if(category_id):
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()
    