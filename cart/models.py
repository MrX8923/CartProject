from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(blank=True)
    image = models.CharField(max_length=50, blank=True)
    discount = models.BooleanField(default=False)
    discount_count = models.FloatField(default=1)

    def __str__(self):
        return self.description


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, default=1)
    total_cost = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return f'{self.product} {self.count} {self.total_cost}'

    def count_total_price(self):
        return self.count * self.product.price


class Order(models.Model):
    address = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=20, blank=True)
    tel = models.CharField(max_length=12, blank=True)
    order_list = models.TextField(blank=True)
    total_cost = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.address} {self.name} {self.tel} {self.total_cost} {self.order_list}'
