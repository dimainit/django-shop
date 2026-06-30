from django.urls import path
from shop.views import index, about, contact, products, product_detail, login_view, register_view, logout_view

urlpatterns = [
    path('', index, name="home_page"),
    path('about/', about, name="about_page"),
    path('contact/', contact, name="contact_page"),
    path('products/', products, name="item_product"),
    path('products/<int:pk>', product_detail, name="products"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout")
]