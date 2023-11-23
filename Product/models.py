from django.db import models


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
