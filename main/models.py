from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    stock = models.IntegerField(default=0)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Menyimpan informasi pemilik produk

    def __str__(self):
        return f"{self.name} - {self.author} ({self.publication_year})"
