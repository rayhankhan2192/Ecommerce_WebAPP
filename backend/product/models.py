from django.db import models
from category.models import Category, SubCategory
from django.utils.text import slugify

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products",)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    descriptions = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    images = models.ImageField(upload_to='photo/products')
    stock = models.IntegerField()
    is_available = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return f'{self.category.slug}/{self.subcategory.slug}/{self.slug}/'
    
    def get_image(self):
        if self.images:
            return 'http://127.0.0.1:8000' + self.images.url
        return ''
