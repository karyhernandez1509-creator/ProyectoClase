from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Product


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("login")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username", ""),
            password=request.POST.get("password", ""),
        )
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")


@login_required
def dashboard(request):
    return render(
        request,
        "dashboard.html",
        {
            "user": request.user,
            "products": Product.objects.all()[:5],
        },
    )


def logout_view(request):
    logout(request)
    return redirect("login")


def product_list_api(request):
    products = Product.objects.all()
    data = [{"name": product.name, "price": product.price} for product in products]
    return JsonResponse(data, safe=False)
