from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    banner = models.ImageField(upload_to="banners")

    def __str__(self):
        return self.title
