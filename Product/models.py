from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(to="self", on_delete=models.SET_NULL, null=True, blank=True, related_name="parent")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(to=ProductCategory, on_delete=models.SET_NULL, null=True, related_name="categories")
    image = models.ImageField("product_img")
    name = models.CharField(max_length=254)
    pricing = models.FloatField()
    warranty = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="customer")
    product = models.ManyToManyField(to=Product)

    def __str__(self):
        return f"{self.user.username}"

    def products(self):
        return ",\t".join([x.name for x in self.product.all()])

    def totals(self):
        total = 0
        for i in self.product.all():
            total += i.pricing
        return total

