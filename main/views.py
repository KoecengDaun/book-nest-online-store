from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

# View untuk halaman utama
def show_main(request):
    # Menampilkan semua produk
    products = Product.objects.all()

    # Menambahkan logika form
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_main')  # Redirect ke halaman yang sama setelah produk ditambahkan
    else:
        form = ProductForm()

    # Menggabungkan context untuk form dan produk
    context = {
        'products': products,
        'app_name': 'BookHub',
        'class_name': 'Laurentius Arlana Farel Mahardika - BookHub Online Store',
        'form': form,  # Tambahkan form ke context
    }
    
    return render(request, 'main.html', context)

# Semua data dalam format JSON
def product_list_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return JsonResponse(data, safe=False)

# Semua data dalam format XML
def product_list_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

# Data JSON berdasarkan ID
def product_detail_json(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = serializers.serialize('json', [product])
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

# Data XML berdasarkan ID
def product_detail_xml(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = serializers.serialize('xml', [product])
        return HttpResponse(data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse('<error>Product not found</error>', content_type='application/xml', status=404)
