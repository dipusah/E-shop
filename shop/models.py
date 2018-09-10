from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    price = models.FloatField(null=True)
    details = RichTextField()
    featured = models.BooleanField()
    brand_name = models.CharField(max_length=200)
    image = models.ImageField()
    view_count = models.BigIntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
