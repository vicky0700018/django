# It IS used to create table in the data base
# Create your models here.
# When Ever we use any image in my model we need to run pip install pillow in the terminal


#Whenever we create a model in models.py we need to run two commands in the terminal
#1. python manage.py makemigrations
#2. python manage.py migrate


from django.db import models

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.category_name


# Product Model
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name


# Student Model
class Student(models.Model):
    std_name = models.CharField(max_length=255)
    std_roll = models.CharField(max_length=50)
    std_image = models.ImageField(upload_to='students/', null=True, blank=True)
    std_email = models.EmailField()
    std_city = models.CharField(max_length=100)

    def __str__(self):
        return self.std_name

