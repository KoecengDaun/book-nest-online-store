from django.db import models

class Product(models.Model):
    # Atribut yang wajib
    name = models.CharField(max_length=255)  # Nama buku
    price = models.IntegerField()  # Harga buku
    description = models.TextField()  # Deskripsi buku

    # Atribut tambahan
    author = models.CharField(max_length=255)  # Penulis buku
    genre = models.CharField(max_length=100)  # Genre buku
    publication_year = models.IntegerField()  # Tahun terbit

    # Atribut opsional
    stock = models.IntegerField(default=0)  # Stok buku
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)  # ISBN buku

    def __str__(self):
        return f"{self.name} - {self.author} ({self.publication_year})"

