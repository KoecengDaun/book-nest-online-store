from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.show_main, name='show_main'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('json/', views.product_list_json, name='product_list_json'),
    path('xml/', views.product_list_xml, name='product_list_xml'),
    path('json/<int:id>/', views.product_detail_json, name='product_detail_json'),
    path('xml/<int:id>/', views.product_detail_xml, name='product_detail_xml'),
]
