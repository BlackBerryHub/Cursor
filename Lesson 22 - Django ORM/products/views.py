from django.shortcuts import render
from .models import Category, Product


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "category.html", {"category": category, "products": category.products.all()})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_detail.html", {"product": product})