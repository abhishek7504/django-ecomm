from django.db import models
from accounts.models import User

class Product(models.Model):
    user = models.ForeignKey('accounts.User',on_delete = models.CASCADE,null=True,blank=True,related_name='accounts_user')
    title = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
    image = models.ImageField(upload_to = 'products/')
    category = models.ForeignKey('Category',on_delete = models.CASCADE)
    available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'categories/')

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.phone_number

