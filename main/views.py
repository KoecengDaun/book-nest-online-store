from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib import messages


@login_required
def show_main(request):
    """Menampilkan produk milik user yang sedang login"""
    products = Product.objects.filter(owner=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # Menetapkan pengguna yang login sebagai pemilik produk
            product.save()
            return redirect('show_main')
    else:
        form = ProductForm()

    context = {
        'products': products,
        'app_name': 'BookHub',
        'class_name': 'Laurentius Arlana Farel Mahardika - BookHub Online Store',
        'form': form,
        'no_products': products.count() == 0
    }
    
    return render(request, 'main.html', context)


# Fungsi untuk edit produk
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        
        # Skip ISBN validation if it belongs to the current product
        if form.is_valid():
            if Product.objects.filter(isbn=form.cleaned_data['isbn']).exclude(id=product.id).exists():
                form.add_error('isbn', 'Product with this ISBN already exists.')
            else:
                form.save()
                return redirect('show_main')
        else:
            print(form.errors)
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'edit_product.html', context)

# Fungsi untuk hapus produk
@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('show_main')
    
    context = {
        'product': product
    }
    return render(request, 'confirm_delete.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user  # Assume products have an owner field
            product.save()
            return redirect('show_main')  # Redirect to the main page after adding product
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'add_product.html', context)

@login_required
def show_all_products(request):
    products = Product.objects.exclude(owner=request.user)  # Menampilkan semua produk kecuali milik user yang sedang login

    context = {
        'products': products,
        'app_name': 'BookHub',
        'class_name': 'Laurentius Arlana Farel Mahardika - BookHub Online Store',
    }
    
    return render(request, 'all_products.html', context)

@login_required
def create_book_ajax(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Assuming you use ProductForm for books
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # Assuming a book is linked to the logged-in user
            book.save()
            return JsonResponse({'status': 'success', 'book': book.name}, status=200)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'invalid method'}, status=405)


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Otomatis login setelah pendaftaran berhasil
            messages.success(request, "Akun berhasil dibuat dan Anda telah login.")
            return redirect('show_main')
        else:
            print(form.errors)  # Debugging untuk melihat kesalahan pada form
            messages.error(request, "Pendaftaran gagal. Silakan coba lagi.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('show_main')  # Redirect ke halaman utama jika login berhasil
            else:
                form.add_error(None, "Username atau password salah.")  # Tampilkan error jika login gagal
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

def product_list_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return JsonResponse(data, safe=False)

def product_list_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

def product_detail_json(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = serializers.serialize('json', [product])
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def product_detail_xml(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = serializers.serialize('xml', [product])
        return HttpResponse(data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse('<error>Product not found</error>', content_type='application/xml', status=404)
