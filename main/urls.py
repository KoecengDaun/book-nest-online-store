from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.show_main, name='show_main'),  # Halaman utama yang menampilkan produk milik user
    path('all-products/', views.show_all_products, name='show_all_products'),  # Halaman untuk menampilkan produk milik pengguna lain
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('json/', views.product_list_json, name='product_list_json'),
    path('xml/', views.product_list_xml, name='product_list_xml'),
    path('json/<int:id>/', views.product_detail_json, name='product_detail_json'),
    path('xml/<int:id>/', views.product_detail_xml, name='product_detail_xml'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('add-product/', views.add_product, name='add_product'),
    path('create-ajax/', views.create_book_ajax, name='create_book_ajax'),
    path('create-flutter/', views.create_product_flutter, name='create_product_flutter'),
]
