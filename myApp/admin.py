from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand', 'category', 'product_image']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']
