from django.db import models
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    descriptions = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    images = models.ImageField(upload_to='photo/products')
    stock = models.IntegerField()
    is_available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return f'{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.images:
            return 'http://127.0.0.1:8000' + self.images.url
        return ''
