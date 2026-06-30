from django.shortcuts import render
from django.http import HttpResponse


products_list = [
    {
        "id": 1,
        "title": "Apple Watch SE 3 (2025)",
        "description": "Apple Watch SE 3 features innovative sensors, including a heart rate monitor and wrist-based temperature reading, to help you stay on top of your health.",
        "price": 5990,
    },
    {
        "id": 2,
        "title": "AirPods Pro 3",
        "description": "Now with groundbreaking active noise cancellation, Note ¹ with all-new heart rate sensing Note ² and a battery life of up to 8 hours.",
        "price": 6499,
    },
    {
        "id": 3,
        "title": "Samsung Galaxy S25 FE 8GB/128GB",
        "description": "Mobile phone - 6.7 AMOLED 2340  1080 (120Hz), storage: 128 GB, RAM: 8 GB,",
        "price": 16900,
    },
    {
        "id": 4,
        "title": "PHILCO PHEM 2250",
        "description": "Lever coffee maker - power input 3200 W, pressure 19 bar, standard portafilter, water tank volume 2.5 l",
        "price": 7990,
    },
    {
        "id": 5,
        "title": "HISENSE",
        "description": "American refrigerator - with drawer, energy class E, refrigerator volume 302 l, freezer volume 178 l",
        "price": 24590,
    },
]

def index(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")

def products(request):
    text = f"<h1>Ваш товар номер: </h1>"
    for item in products_list:
        text += f"{item['id']} - {item['title']}<br>"
    return HttpResponse(text)

def product_detail(request, pk):
    for item in products_list:
        if item["id"] == pk:
            return HttpResponse(f"Товар номер: {item['id']} - {item['title']} - {item['description']} - {item['price']}Kč")
    return HttpResponse("Товар не найден")


def login_view(request):
    return HttpResponse("Login Page")

def register_view(request):
    return HttpResponse("Register Page")

def logout_view(request):
    return HttpResponse("Logout Page")
