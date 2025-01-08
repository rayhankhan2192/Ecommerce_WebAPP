from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    category_image = models.ImageField(upload_to='photo/categories', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    subcategory_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.subcategory_name)
        super(SubCategory, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
    
    def __str__(self):
        return self.subcategory_name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'