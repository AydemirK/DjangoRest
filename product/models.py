from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.name
    
    
    def products_count(self):
        return self.product_set.all().count()
    
class Product(models.Model):
    title = models.CharField(max_length=150)
    description =  models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
        
    def __str__(self):
        return self.title
    
    
    
STARS =[(i, str(i)) for i in range(1, 6)]
    
    
class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=1)
    
    def __str__(self):
        return f'Review for {self.product.title}'