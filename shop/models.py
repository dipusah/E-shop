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

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Slider(models.Model):
    image = models.ImageField(upload_to='slides')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption
