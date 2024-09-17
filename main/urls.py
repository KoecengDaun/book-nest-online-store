from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main, name='show_main'),  # Halaman utama dengan form dan daftar produk
    path('json/', views.product_list_json, name='product_list_json'),  # Semua produk dalam format JSON
    path('xml/', views.product_list_xml, name='product_list_xml'),  # Semua produk dalam format XML
    path('json/<int:id>/', views.product_detail_json, name='product_detail_json'),  # Produk spesifik dalam format JSON
    path('xml/<int:id>/', views.product_detail_xml, name='product_detail_xml'),  # Produk spesifik dalam format XML
]


