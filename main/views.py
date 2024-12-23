from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
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


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('show_main'))
    context = {'form': form}
    return render(request, "product/edit_product.html", context)

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
    return render(request, 'product/confirm_delete.html', context)

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
    return render(request, 'product/add_product.html', context)

@login_required
def show_all_products(request):
    products = Product.objects.exclude(owner=request.user)  # Menampilkan semua produk kecuali milik user yang sedang login

    context = {
        'products': products,
        'app_name': 'BookHub',
        'class_name': 'Laurentius Arlana Farel Mahardika - BookHub Online Store',
    }
    
    return render(request, 'product/all_products.html', context)



def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product/product_detail.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show_main')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response = redirect('show_main')
                response.set_cookie('last_login', str(request.user.last_login))  # Set cookie last_login
                return response
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

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
