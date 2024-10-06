from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'author', 'genre', 'publication_year', 'description', 'stock', 'isbn']

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        # Check if another product (different id) has the same ISBN
        if Product.objects.filter(isbn=isbn).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Product with this ISBN already exists.")
        return isbn

