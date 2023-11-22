from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('F', "Feature Section"),
    ('A', "About Us"),
    ('HA', "Home Appliances"),
    ('G', "Cosmetics Gadget"),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models. CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='produtimg')

    def __str__(self):
        return str(self.id)
    

class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.id)