from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"
