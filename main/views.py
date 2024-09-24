from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def show_main(request):
    products = Product.objects.all()  # Menampilkan semua produk yang ada

    # Logika untuk menambahkan produk baru
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
    }
    
    return render(request, 'main.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show_main')
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
                response = redirect('show_main')
                response.set_cookie('last_login', str(request.user.last_login))  # Set cookie last_login
                return response
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
