from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()
    context = {
        'products': products,  # Ubah 'books' menjadi 'products'
        'app_name': 'BookHub',
        'class_name': 'Laurentius Arlana Farel Mahardika - BookHub Online Store',
    }
    return render(request, 'main.html', context)


