from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from products.models import Product


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SliderItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.title


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.address


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
    price = models.IntegerField()
    price_with_discount = models.IntegerField()
    def __str__(self):
        return str(self.order.id) + " " + self.product.title


class Coupon(models.Model):
    code = models.CharField(max_length=32, unique=True)
    discount = models.IntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    active = models.BooleanField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        return self.code