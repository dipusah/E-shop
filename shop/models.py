from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    price = models.FloatField(null=True)
    details = RichTextField()
    featured = models.BooleanField()
    brand_name = models.CharField()
    image = models.ImageField()
    view_count = models.BigIntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




