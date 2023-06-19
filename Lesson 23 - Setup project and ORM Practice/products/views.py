from django.shortcuts import render
from .models import Category


def category_page(request, slug):
    sort_by = request.GET.get('sort')
    category = Category.objects.get(slug=slug)
    if sort_by == "price":
        products = category.products.order_by('price')
    elif sort_by == "date":
        products = category.products.order_by('-date_added')
    else:
        products = category.products.all()
    return render(request, "category.html", {"category": category, "products": products})
