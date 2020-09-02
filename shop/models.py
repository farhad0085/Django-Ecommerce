from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=260)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_picture = models.ImageField(upload_to='product_pictures', default='default-product.jpg')
    categories = models.ManyToManyField(ProductCategory)
    
    def __str__(self):
        return f"{self.id} - {self.product_name}"

class ProductReview(models.Model):
    author_name = models.CharField(max_length=30)
    author_email = models.EmailField()
    review_description = models.TextField(blank=True)
    review_score = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author_name} - {self.review_score}"